import logging as log

log.basicConfig(
    level=log.DEBUG, 
    format=str(
        '%(asctime)s - %(levelname)s [%(filename)s]:%(lineno)s - %(message)s'),
         datefmt='%d/%m/%Y %I:%M:%S %p', 
    handlers=[
        log.FileHandler('pip-log.txt', 'a', 'utf-8'),
        log.StreamHandler()
    ]
)

if __name__ == '__main__':
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')