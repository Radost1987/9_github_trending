from datetime import datetime, timedelta
import requests


def get_date():
    time_interval_in_days = 7
    date = datetime.today() - timedelta(days=time_interval_in_days)
    return str(date.date())


def get_trending_repositories(drawdown_period):
    number_of_trending_repositories = 20
    payload = {'q': 'created:>{}'.format(drawdown_period),
               'sort': 'stars',
               'order': 'desc'
              }
    github_info_repositories = requests.get('https://api.github.com/search/repositories',
                                            params=payload)
    list_of_trending_repositories = \
        github_info_repositories.json()['items'][:number_of_trending_repositories]
    return list_of_trending_repositories

if __name__ == '__main__':
    period = get_date()
    try:
        trending_repositories = get_trending_repositories(period)
    except requests.RequestException:
        print('Something is wrong. Try again')
    else:
        print('20 trending repositories of GitHub for last week\n')
        for repositories in trending_repositories:
            print(
                'Repositories name: {}\n'
                'Repositories url: {}\n'
                'Repositories open issues: {}\n'
                'Repositories stargazers count: {}\n'.format(repositories['name'],
                                                             repositories['html_url'],
                                                             repositories['open_issues'],
                                                             repositories['stargazers_count']
                                                             )
            )
