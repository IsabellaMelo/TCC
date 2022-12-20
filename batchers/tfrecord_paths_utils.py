from __future__ import annotations

from collections.abc import Iterable
import glob
import os
import pickle
from typing import Optional

import numpy as np

from batchers.dataset_constants import TOTAL_SIZE, SIZES, SURVEY_NAMES


ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
IDHM_TFRECORDS_PATH_ROOT = '/content/drive/MyDrive/USP/TCC/data/images/idhm_tfrecords_2/'


def idhm() -> np.ndarray:
    '''Gets a list of paths to all TFRecord files comprising the VR dataset.
    Returns: np.array of str, sorted paths to TFRecord files
    '''
    return idhm_ooc(split='all', dataset='IDHM_OOC_A')
    
def idhm_ooc(dataset: str, split: str) -> np.ndarray:
    '''Gets a list of paths to TFRecords corresponding to the given split of
    a desired DHS dataset.
    Args
    - dataset: str, has format 'DHS_OOC_X' where 'X' is one of ['A', 'B', 'C', 'D', 'E']
    - splits: str, one of ['train', 'val', 'test', 'all']
    Returns: np.array of str, sorted paths to TFRecord files
    '''
    if split == 'all':
        splits = ['train', 'val', 'test']
    else:
        splits = [split]

    survey_names = SURVEY_NAMES[dataset]
    tfrecord_paths = []
    for s in splits:
        for municipality_year in survey_names[s]:
            glob_path = os.path.join(IDHM_TFRECORDS_PATH_ROOT, municipality_year, '*.tfrecord.gz')
            tfrecord_paths += glob.glob(glob_path)
    assert len(tfrecord_paths) == SIZES[dataset][split]
    return np.sort(tfrecord_paths)