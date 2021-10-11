import logging as log

# el debug es el mas bajo
log.basicConfig(
    level=log.DEBUG, 
    format=str(
        '%(asctime)s - %(levelname)s [%(filename)s]:%(lineno)s - %(message)s'),
         datefmt='%d/%m/%Y %I:%M:%S %p', 
    handlers=[
        log.FileHandler('log.txt', 'a', 'utf-8'),
        log.StreamHandler()
    ]
)

# pruebas dentro del archivo

if __name__ == '__main__':
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')