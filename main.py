from tae_celery_pac import tae_server

if __name__ == '__main__':
    tae_server.app.worker_main(argv = ['worker', '--loglevel=info'])