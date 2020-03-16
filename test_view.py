import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

class Parser:
    headers = {"accept":"*/*" ,"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def __init__(self, home, catalog):
        self.home = home 
        self.catalog = catalog
        self.session = requests.Session()
        self.category_url = []
        self.concrete_category_url = []
        self.concrete_category_info = []

    def check_connection_home(self):
        
        request = self.session.get(self.home, headers=self.headers)
        if request.status_code == 200:
            print('Home check: SUCCESS')
            return True
        else:
            print('Home check: FAIL')
            return False

        

    def check_connection_catalog(self):
        
        request = self.session.get(self.catalog, headers=self.headers)
        if request.status_code == 200:
            print('Catalog check: SUCCESS')
            return True
        else:
            return False
        

    def get_all_category_from_catalog(self):
        if self.check_connection_catalog() and self.check_connection_home():
            request = self.session.get(self.catalog, headers=self.headers)
            soup = bs(request.content, "lxml")
            card_divs = soup.find_all("div", attrs= {"class":"CategoryCards__item CategoryCards__item--col-xs-1-2 CategoryCards__item--col-md-1-3 CategoryCards__item--col-lg-1-4"})
            print('Starting get all categories')
            for card in tqdm(card_divs):
                try:
                    card_category_name = card.find('h2', attrs={'class':'CategoryCard__title H3'}).text.strip()
                    card_category_url = card.find('a',attrs={'class':'CategoryCard__link'})['href'].strip().split('/')[2] +'/'
                    self.category_url.append(
                        {
                            'name': card_category_name,
                            'url' : self.catalog + card_category_url,
                        }
                    )
                except:
                    print('ERROR while Parsing. Skipped')

    def check_all_items_from_category_connection(self, request):
        #request = self.session.get(item_url, headers=self.headers)
        if request.status_code == 200:
            return True 
        return False

    def build_all_urls(self):
        #self.get_all_category_from_catalog()
        print('Start Building AllCategoryCatalog')
        for temp in tqdm(self.category_url): 
            base_link = temp['url']
            self.get_all_items_from_category(base_link)
            #break
            

    def get_all_items_from_category(self, base_link):
            isFirstItem = True
            #replace to full category_url
            

            request = self.session.get(base_link, headers=self.headers)
            if self.check_all_items_from_category_connection(request):
                soup = bs(request.content, 'lxml')
                link_list = []
                list_items_divs = soup.find_all('div' , attrs={'class' : 'ProductsSection__container Section__container Container'})
                for items_row in list_items_divs:
                    try:
                        all_items_title = items_row.find('h2', attrs={'class' : 'Section__title'}).text
                        all_items_link  =items_row.find('header', attrs={'class' : 'Section__header'})['onclick'].split('location.href=')[1].strip("'").split('/')[-2] + '/'
                        if isFirstItem:
                            link_list =  [{all_items_title : base_link + all_items_link}]
                            isFirstItem = False 
                        else:
                            link_list.append({all_items_title :base_link + all_items_link})
                        #print(temp)
                    except:
                        pass
                self.concrete_category_url.append(link_list)

    def parse_items_with_price(self):
        self.build_all_urls()
        print('ALMOST DONE')
        for temp in tqdm(self.concrete_category_url):
            for pair in temp:
                for k, v in pair.items():
                    category_name = k 
                    category_url = v
                self.concrete_category_info.append(
                            {
                                'category_name': category_name,
                                'category_url': category_url,
                                'items' : [],
                            }
                        )

                request = self.session.get(category_url, headers=self.headers)
                if self.check_all_items_from_category_connection(request):
                    soup = bs(request.content, 'lxml')
                    product_card_divs = soup.find_all('div', attrs={'class':'ProductCards__item ProductCards__item--col-lg-1-3'})
                    for product in product_card_divs:
                        try:
                            name = product.find('a', attrs={'class':'ProductCard__link'})['title']
                            rating = product.find('div', attrs={'class':'Rating__text'}).text
                            price = product.find('span', attrs={'class':'Price__value'})['content'].strip()
                            self.concrete_category_info[-1]['items'].append(
                                {
                                    'name':name,
                                    'rating':rating,
                                    'price': price,
                                }
                            )
                        except:
                            pass
                

        



    def __del__(self):
        self.session.close()
        print('Session close: SUCCESS')



if __name__== '__main__':
    HOME_URL = 'https://vkusvill.ru/'
    CATALOG_URL = 'https://vkusvill.ru/goods/'

    parser = Parser(HOME_URL, CATALOG_URL)


    parser.parse_items_with_price()
    for cat in parser.concrete_category_info:
        print("####################")
        print(cat['category_name'], cat['category_url'])
        

        for item in cat['items']:
            print(item)
            break