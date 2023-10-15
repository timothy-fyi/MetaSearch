from bs4 import BeautifulSoup
import requests

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
        return print('Result not found. Please try again.')

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

    # user_search_url = 'https://www.metacritic.com' + page_links[0]

    search_results_page = requests.get(user_search_url, headers={'User-Agent': 'Mozilla/5.0'}).text
    results_soup = BeautifulSoup(search_results_page, "html.parser")

    search_title = results_soup.find('div', class_= 'c-productHero_title').text
    try:
        search_description = results_soup.find('span', class_= 'c-productionDetailsGame_description').text
    except AttributeError:
        search_description = results_soup.find('span', class_= 'c-productDetails_description').text
    search_critic_score = results_soup.find('div', class_= 'c-siteReviewScore_background-critic_medium').text
    search_user_score = results_soup.find('div', class_= 'c-siteReviewScore_user').text
    try:
        search_type = results_soup.find('div', attrs={'class': 'c-pageProduct'})['type']
        if search_type == 'movie':
            meta_data = []
            search_meta_data = results_soup.find('div', class_= 'c-heroMetadata')
            for meta in search_meta_data.find_all('span'):
                meta_data.append(meta.text.strip())
            run_time = meta_data[-1]
    except:
        pass

    try:
        print(
            f'''Title: {search_title.strip()}
Run Time: {run_time}\n
Critic Score: {search_critic_score.strip()}
User Score: {search_user_score.strip()}\n
Description: {search_description.strip()}
            '''
        )
    except NameError:
        print(
            f'''Title: {search_title.strip()}\n
Critic Score: {search_critic_score.strip()}
User Score: {search_user_score.strip()}\n
Description: {search_description.strip()}
            '''
        )