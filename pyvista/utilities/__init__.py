"""Utilities routines."""
from .errors import (
    GPUInfo,
    Observer,
    Report,
    assert_empty_kwargs,
    get_gpu_info,
    send_errors_to_logging,
    set_error_output_file,
    check_valid_vector,
    VtkErrorCatcher,
)
from .features import *
from .fileio import *
from .geometric_objects import *
from .helpers import *
from .parametric_objects import *
from .sphinx_gallery import Scraper, _get_sg_image_scraper
from .regression import compare_images
from . import transformations
from .xvfb import start_xvfb
from .reader import (
    get_reader,
    AVSucdReader,
    BaseReader,
    BinaryMarchingCubesReader,
    BMPReader,
    BYUReader,
    CGNSReader,
    DEMReader,
    EnSightReader,
    FacetReader,
    FluentReader,
    GLTFReader,
    HDFReader,
    HDRReader,
    JPEGReader,
    MetaImageReader,
    MFIXReader,
    MultiBlockPlot3DReader,
    NRRDReader,
    OBJReader,
    OpenFOAMReader,
    Plot3DMetaReader,
    PLYReader,
    PNGReader,
    PNMReader,
    PointCellDataSelection,
    PTSReader,
    PVDDataSet,
    PVDReader,
    SegYReader,
    SLCReader,
    STLReader,
    TIFFReader,
    TimeReader,
    VTKDataSetReader,
    VTKPDataSetReader,
    XMLImageDataReader,
    XMLPImageDataReader,
    XMLRectilinearGridReader,
    XMLPRectilinearGridReader,
    XMLUnstructuredGridReader,
    XMLPUnstructuredGridReader,
    XMLPolyDataReader,
    XMLStructuredGridReader,
    XMLMultiBlockDataReader,
    DICOMReader,
)
