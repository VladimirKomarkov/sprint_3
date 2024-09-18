import logging

logging.basicConfig(filename='app.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('Это сообщение для отладки')
logging.info('Информационное сообщение')
logging.warning('Предупреждение')
logging.error('Ошибка')
logging.critical('Критическая ошибка')