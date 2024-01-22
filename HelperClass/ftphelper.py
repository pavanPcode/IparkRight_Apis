from ftplib import FTP
import os
import configparser

def read_ftp_config(config_path='/ftpConfig.ini', ftp_name='ftp_server'):
    config = configparser.ConfigParser()
    config.read(config_path)
    ftp_info = {
        'host': config.get(ftp_name, 'host'),
        'user': config.get(ftp_name, 'user'),
        'password': config.get(ftp_name, 'password'),
    }
    return ftp_info

def upload_to_ftp(local_filename, remote_folder, config_path='/ftpConfig.ini', ftp_name='ftp_server'):
    ftp_info = read_ftp_config(config_path=config_path, ftp_name=ftp_name)

    with FTP(ftp_info['host']) as ftp:
        ftp.login(user=ftp_info['user'], passwd=ftp_info['password'])
        with open(local_filename, 'rb') as local_file:
            remote_filename = os.path.join(remote_folder, os.path.basename(local_filename))
            ftp.storbinary(f"STOR {remote_filename}", local_file)

if __name__ == '__main__':
    # Example usage
    # Replace 'local_file_path' and 'remote_file_folder' with your actual file paths and folder
    upload_to_ftp('local_file_path', 'remote_file_folder')
