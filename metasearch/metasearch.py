from bs4 import BeautifulSoup
import requests
import re

def metasearch(search_term):

    url = 'https://www.metacritic.com/search/' + search_term + '"'

    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    soup = BeautifulSoup(req, "html.parser")

    page_links = []
    search_results = soup.find('div', class_= 'c-pageSiteSearch-results')
    try:
        for a in search_results.find_all('a', href = True):
            if a.text:
                page_links.append(a['href'])
    except AttributeError:
        return print('\nResult not found. Please try again.')

    page_titles = []
    search_results_two = soup.find_all('p', class_= 'g-text-medium-fluid')
    for result in search_results_two:
        if result.text.lower().strip() == search_term:
            index_position = search_results_two.index(result)
            user_search_url = 'https://www.metacritic.com' + page_links[index_position]
            break
        else:
            index_position = 0
            user_search_url = 'https://www.metacritic.com' + page_links[index_position]

    search_results_page = requests.get(user_search_url, headers={'User-Agent': 'Mozilla/5.0'}).text
    results_soup = BeautifulSoup(search_results_page, "html.parser")

    try:
        search_title = results_soup.find('div', class_= 'c-productHero_title').text
    except AttributeError:
        return print('\nYour search was not for a valid game, movie, or TV show. Please try again.')
    
    try:
        search_description = results_soup.find('span', class_= 'c-productionDetailsGame_description').text
    except AttributeError:
        search_description = results_soup.find('span', class_= 'c-productDetails_description').text

    search_critic_score = results_soup.find('div', class_= 'c-siteReviewScore_background-critic_medium').text
    search_user_score = results_soup.find('div', class_= 'c-siteReviewScore_user').text

    regex = re.compile('.*c-pageProduct.*')
    search_type = results_soup.find('div', attrs={'class': regex})['type']

    if search_type == 'movie':
        meta_data = []
        search_meta_data = results_soup.find('div', class_= 'c-heroMetadata')
        for meta in search_meta_data.find_all('span'):
            meta_data.append(meta.text.strip())
        release_year = meta_data[0]
        rating = meta_data[1]
        run_time = meta_data[-1]
        print(
            f'\nTitle: {search_title.strip()}\n'
            f'Release Year: {release_year}\n'
            f'Rated: {rating}\n'
            f'Run Time: {run_time}\n\n'
            f'Critic Score: {search_critic_score.strip()}\n'
            f'User Score: {search_user_score.strip()}\n\n'
            f'Description: {search_description.strip()}\n'
        )

    elif search_type == 'game':
        try:
            game_release_date = results_soup.find('div', class_= 'c-gameDetails_ReleaseDate').text
        except AttributeError:
            return print('\nYour search was not for a valid game, movie, or TV show. Please try again.')
        print(
            f'\nTitle: {search_title.strip()}\n'
            f'{game_release_date}\n\n'
            f'Critic Score: {search_critic_score.strip()}\n'
            f'User Score: {search_user_score.strip()}\n\n'
            f'Description: {search_description.strip()}\n'
        )

    elif search_type == 'tv':
        tv_details = []
        search_tv_details = results_soup.find('div', class_= 'c-productionDetailsTv')
        for details in search_tv_details.find_all('span'):
            tv_details.append(details.text.strip())
        tv_release_date = tv_details[3]
        tv_num_seasons = tv_details[5]
        print(
            f'\nTitle: {search_title.strip()}\n'
            f'Release Date: {tv_release_date}\n'
            f'Seasons: {tv_num_seasons}\n\n'
            f'Critic Score: {search_critic_score.strip()}\n'
            f'User Score: {search_user_score.strip()}\n\n'
            f'Description: {search_description.strip()}\n'
        )
    else:
        return print('\nSearch type not valid. Please try again.')
