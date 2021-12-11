import logging
logging.basicConfig(level=logging.INFO)
import subprocess

logger = logging.getLogger(__name__)
news_sites_uids = ['eluniversal', 'elpais']

def main():
    _extract()
    _transform()
    _load()

def _extract():
    logger.info('Starting extract process')
    for news_site_uid in news_sites_uids:
        subprocess.run(['python', 'main.py', news_site_uid], cwd='./Extract')
        subprocess.run(['find', '.', '-name', '{}*'.format(news_site_uid), \
            '-exec', 'mv', '{}', '../Transform/{}_.csv'.format(news_site_uid), ';'], cwd='./Extract')

def _transform():
    logger.info('Starting Transform Process')
    for new_site_uid in news_sites_uids:
        dirty_data_filename = '{}_.csv'.format(new_site_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./Transform')
        subprocess.run(['rm', dirty_data_filename], cwd='./Transform')
        subprocess.run(['mv', clean_data_filename, '../Load/{}.csv'.format(new_site_uid)], cwd='./Transform')

def _load():
    logger.info('Starting load process')
    for new_site_uid in news_sites_uids:
        clean_data_filename = '{}.csv'.format(new_site_uid)
        subprocess(['python', 'main.py', clean_data_filename], cwd='./Load')
        subprocess(['rm', clean_data_filename], cwd='./Load')

if __name__=='__main__':
    main()