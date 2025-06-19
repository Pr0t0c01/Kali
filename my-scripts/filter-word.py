#! /usr/bin/python3

import argparse

def remove_lines_with_keywords(url_list, keywords, max_char_count):
    filtered_list = [url for url in url_list if all(keyword not in url for keyword in keywords)]
    return filtered_list

def main(file_path, keywords_to_remove, max_char_count, output_textfile):
    # Read the URLs from the file
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    # Remove leading/trailing whitespaces from keywords
    keywords_to_remove = [keyword.strip() for keyword in keywords_to_remove]

    filtered_urls = remove_lines_with_keywords(urls, keywords_to_remove, max_char_count)

    # Save filtered URLs to a text file
    with open(output_textfile, 'w') as output_file:
        for url in filtered_urls:
            output_file.write(url + '\n')

    print("Filtered URLs have been saved to:", output_textfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter URLs based on keywords and character count')
    parser.add_argument('file_path', help='File path containing the URLs')
    parser.add_argument('keywords_to_remove', help='Keywords to remove (separated by comma)')
    parser.add_argument('output_textfile', help='Output text filename')
    args = parser.parse_args()

    keywords_to_remove = args.keywords_to_remove.split(',')
    main(args.file_path, keywords_to_remove, 300, args.output_textfile)
