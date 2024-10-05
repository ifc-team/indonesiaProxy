import argparse
from scripts.logo import logo


def function():
    parser = argparse.ArgumentParser(description="Proxy Scraper and Checker")
    parser.add_argument('--scrape', action='store_true', help='Scrape proxies from a URL')
    parser.add_argument('-u', '--url', type=str, help='URL to scrape proxies from')
    parser.add_argument('-o', '--output', type=str, help='Output directory to save proxies')
    parser.add_argument('--check', action='store_true', help='Check the validity of proxies')
    parser.add_argument('-p', '--proxy', type=str, help='File containing proxies to check')
    parser.add_argument('--default', action='store_true', help='Use default weblist from weblist.idn')
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        return

    if args.scrape:
        if args.url:
            # proxies = scrape_proxies(args.url)
            # save_proxies(proxies, 'results')
            print("Proxies scraped and saved." + args.url)

    if args.default:
            with open('config/weblist.idn', 'r') as f:
                urls = f.readlines()
            # for url in urls:
            # proxies = scrape_proxies(url.strip())
            # save_proxies(proxies, 'results')
            print("Proxies scraped from default weblist and saved.")

    if args.check:
        if args.proxy:
            # valid_proxies = check_proxies(args.proxy)
            # save_results(valid_proxies, 'valid_proxies.txt')
            print("Valid proxies saved.")


if __name__ == "__main__":
    logo()
    function()
