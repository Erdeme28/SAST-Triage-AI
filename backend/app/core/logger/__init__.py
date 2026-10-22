import atexit
import json
import logging.config
import pathlib
from . import formatters

logger = logging.getLogger("backend_logger")

def setup_logging():
    current_dir = pathlib.Path(__file__).parent
    config_file = current_dir / "config.json"
    
    with open(config_file) as f_in:
        config = json.load(f_in)
        
    logging.config.dictConfig(config)
    
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)
