# encoding: utf-8
"""
Run Fiji is just ImageJ macros headless with python.
"""
import pydebug, subprocess, os, fijibin
from tempfile import NamedTemporaryFile

# debug with DEBUG=fijibin python script.py
debug = pydebug.debug('fijibin')

_bin = fijibin.BIN

##
# Running macros
##
def run(macro, output_files=[], force_close=True):
    """
    Runs Fiji with the suplied macro. Output of Fiji can be viewed by
    setting environment variable `DEBUG=fijibin`.

    Parameters
    ----------
    macro : string or list of strings
        IJM-macro(s) to run. If list of strings, it will be joined with
        a space, so all statements should end with ``;``.
    output_files : list
        Files to check if exists after macro has been run. Files specified that
        do not exist after macro is done will print a warning message.
    force_close : bool
        Will add ``eval("script", "System.exit(42);");`` to end of macro. Exit
        code 42 is used to overcome that errors in macro efficiently will exit
        Fiji with error code 0. In other words, if this line in the macro is
        reached, the macro has most probably finished without errors. This
        is the default behaviour.

        One should also note that Fiji doesn't terminate right away if
        ``System.exit()`` is left out, and it may take several minutes for
        Fiji to close.

    Returns
    -------
    int
        Files from output_files which exists after running macro.
    """
    if type(macro) == list:
        macro = ' '.join(macro)
    if len(macro) == 0:
        print('fijibin.macro.run got empty macro, not starting fiji')
        return
    if force_close:
        # make sure fiji halts immediately when done
        # hack: use error code 42 to check if macro has run sucessfully
        macro = macro + 'eval("script", "System.exit(42);");'

    debug('macro {}'.format(macro))

    # avoid verbose output of Fiji when DEBUG environment variable set
    env = os.environ.copy()
    debugging = False
    if 'DEBUG' in env:
        if env['DEBUG'] == 'fijibin' or env['DEBUG'] == '*':
            debugging = True
        del env['DEBUG']

    with NamedTemporaryFile(mode='w', suffix='.ijm') as m:
        m.write(macro)
        m.flush() # make sure macro is written before running Fiji

        cmd = [_bin, '--headless', '-macro', m.name]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, env=env)
        out, err = proc.communicate()

        for line in out.decode('latin1', errors='ignore').splitlines():
            debug('stdout:' + line)
        for line in err.decode('latin1', errors='ignore').splitlines():
            debug('stderr:' + line)

    if force_close and proc.returncode != 42:
        print('fijibin ERROR: Fiji did not successfully ' +
              'run this macro: {}.'.format(macro))
        if not debugging:
            print('fijibin Try running script with ' +
                  '`DEBUG=fijibin python your_script.py`')

    # check output_files
    for i,filename in enumerate(output_files):
        if not os.path.isfile(filename):
            print('fijibin ERROR missing output file {}'.format(filename))
            del output_files[i]

    return output_files


##
# Collection of macros
##
def stitch(folder, filenames, x_size, y_size, output_filename,
                 x_start=0, y_start=0, overlap=10):
    """
    Creates a Fiji Grid/Collection stitching macro. Parameters are the same as
    in the plugin and are described in further detail here:
    http://fiji.sc/Image_Stitching#Grid.2FCollection_Stitching.

    **Default stitch parameters:**

    * Filename defined positions
    * Compute overlap
    * Subpixel accurancy
    * Save computation time (but use more RAM)
    * Fusion method: Linear blending
    * Regression threshold: 0.30
    * Max/avg displacement threshold: 2.50
    * Absolute displacement threshold: 3.50


    Parameters
    ----------
    folder : string
        Path to folder with images or folders with images.
        Example: */path/to/slide--S00/chamber--U01--V02/*
    filenames : string
        Filenames of images.
        Example: *field-X{xx}-Y{yy}/image-X{xx}-Y{yy}.ome.tif*
    x_size : int
        Size of grid, number of images in x direction.
    y_size : int
        Size of grid, number of images in y direction.
    output_filename : string
        Where to store fused image. Should be `.png`.
    x_start : int
        Which x position grid start with.
    y_start : int
        Which y position grid start with.
    overlap : number
        Tile overlap in percent. Fiji will find the optimal overlap, but a
        precise overlap assumption will decrase computation time.

    Returns
    -------
    string
        IJM-macro.
    """

    macro = []
    macro.append('run("Grid/Collection stitching",')
    macro.append('"type=[Filename defined position]')
    macro.append('order=[Defined by filename         ]')
    macro.append('grid_size_x={}'.format(x_size))
    macro.append('grid_size_y={}'.format(y_size))
    macro.append('tile_overlap={}'.format(overlap))
    macro.append('first_file_index_x={}'.format(x_start))
    macro.append('first_file_index_y={}'.format(y_start))
    macro.append('directory=[{}]'.format(folder))
    macro.append('file_names={}'.format(filenames))
    macro.append('output_textfile_name=TileConfiguration.txt')
    macro.append('fusion_method=[Linear Blending]')
    macro.append('regression_threshold=0.30')
    macro.append('max/avg_displacement_threshold=2.50')
    macro.append('absolute_displacement_threshold=3.50')
    macro.append('compute_overlap')
    macro.append('subpixel_accuracy')
    macro.append('computation_parameters=[Save computation time (but use more RAM)]')
    # use display, such that we can specify output filename
    # this is 'Fused and display' for previous stitching version!!
    macro.append('image_output=[Fuse and display]");')
    # save to png
    macro.append('selectWindow("Fused");')
    macro.append('saveAs("PNG", "{}");'.format(output_filename))
    macro.append('close();')

    return ' '.join(macro)
