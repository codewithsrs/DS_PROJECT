import os
from box.exceptions import BoxValueError
import yaml
from classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path to yaml : path like input

    Raises:
        valueError: if yaml file is empty
        e: empty file

    Returns:
        configbox: configbox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def save_json(path:Path, data:dict):
    """
    save json data
    
    Args:
        path(path): path to json file
        data(dict): data to be saved in json file

    """

    with open(path,"w") as f:
        json.dump(data, f, indent = 4)

    logger.info(f"json file saved at {path}")