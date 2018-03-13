import sys
import json
import re

def clean_secret(secret, retain_last=False):
    i = 0
    cleaned_secret = ''
    for c in secret:
        if i < len(secret) - 6:
            cleaned_secret += '*'
        else:
            cleaned_secret += c
    return cleaned_key

def main():
    if len(sys.argv) != 3:
        print("please include the path to the config file as the first argument and the path to the cleaned file as the second")
        sys.exit(1)
    config_file_path=sys.argv[1]
    cleaned_conig_file_path=sys.argv[2]
    with open(config_file, 'r') as f:
        config_file = f.read()

    config_json = json.loads(config_file)
    config_json['ClientSecret'] = clean_secret(config_json['ClientSecret'])
    config_json['DataDogAPIKey'] = clean_secret(config_json['DataDogAPIKey'], retain_last=True)

    with open(cleaned_conig_file_path, 'w') as f:
        f.write(json.dumps(config_json))

if __name__ == '__main__':
    main()
