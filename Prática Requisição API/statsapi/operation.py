from loguru import logger

def op_mean(data):
    return sum(data)/len(data)

def op_max(data):
    return max(data)

def op_min(data):
    logger.debug(f"data: '{data}'")
    return min(data)

