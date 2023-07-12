import time

import pandas as pd
from scrapingbee import ScrapingBeeClient
import requests
import json
import datetime
import csv
import time

try:
    with open('stockx_page_prd.csv','a',newline='',encoding='UTF-8') as fp:
        writer = csv.writer(fp)
        writer.writerow([
            'Sr.no',
            'Page No',
            'Rank',
            'product name',
            'product brand',
            'product colour',
            'Product_id',
            'product url',
            'model',
            'type',
            'category',
            'listing type',
            'product price',
            'currency code',
            'product release date',
            'lowest ask',
            'last highest bid time',
            'last lowest ask time',
            'last sale',
            'last sale date',
            'this sale',
            'change value',
            'change percentage',
            'voltality',
            'premium price',
            'product sold',
            'product avg price',
            'product last90 avr price',
            'product desp',
            'product img url',
            'crawled date'
        ])
except:
    pass

sr_no = 0
pg_no = 0
for i in range(1,26):
    pg_no += 1
    headers = {
        'authority': 'stockx.com',
        'accept': '*/*',
        'accept-language': 'en-US',
        'apollographql-client-name': 'Iron',
        'apollographql-client-version': '2023.03.26.03',
        'app-platform': 'Iron',
        'app-version': '2023.03.26.03',
        'content-type': 'application/json',
        # 'cookie': 'language_code=en; stockx_device_id=bc75ea53-9db9-4758-9657-8d68d423894e; _pxvid=45e15e1d-d47b-11ed-87b9-6c6c5a666842; __pxvid=472c1cf5-d47b-11ed-a31c-0242ac120003; _gid=GA1.2.1633532558.1680786155; _gcl_au=1.1.899371660.1680786172; _ga=GA1.2.1851267880.1680786155; __ssid=c9f659f8cc1713c138492bb4ed7d47c; rskxRunCookie=0; rCookie=inmmzf52gkpaf5usivdy0hlg54ow8g; __pdst=161c6e961ff24d439533e8a401969760; _rdt_uuid=1680786269149.ccac77e1-9003-4ad3-88e1-e8a5dc92bccd; ajs_anonymous_id=c780d477-af48-4bab-acc2-ab090a20cc28; QuantumMetricUserID=ce2779c7e63179b213b31048d6a50398; rbuid=rbos-09787b14-429b-4a3f-a239-cf31bb0910b7; ajs_user_id=e42237f0-3842-11ed-97cc-0a0fc094c9a6; _pin_unauth=dWlkPU1EZzFaV00wTkdVdE9UVXhNeTAwT1dWaUxUazNPR0V0TVRGaVpEaGtPRE15TURkbQ; OptanonAlertBoxClosed=2023-04-06T13:23:11.698Z; ftr_ncd=6; tracker_device=ec426991-3857-4742-8e30-69d217659c99; stockx_homepage=sneakers; stockx_selected_region=IN; pxcts=e9ee05cd-d508-11ed-944c-6a6a69696e65; IR_gbd=stockx.com; stockx_preferred_market_activity=sales; stockx_product_visits=2; _ga=GA1.2.1851267880.1680786155; ftr_blst_1h=1680856029708; stockx_session_id=cb0e3be8-852d-4010-972b-c2440573f85d; _ga_TYYSNQDG4W=GS1.1.1680859346.7.0.1680859346.0.0.0; stockx_session=7a7d53bd-5da5-485f-a0d4-d9683b277df7; __cf_bm=hO6c7wf4NVdg_N4KruooNYiaDLvvjzeRBkVkCP4wm5c-1680859998-0-AShwJdVG23dquVU4GPxmUI3GKiKqS3oCoEEECpscxpxYj/V36zYZiHB6AFtfgg5eLfNgeN1BlnmWmUDF+mmIPDM=; _px3=13c0a4c714ee7cd67f3dd1d4c80cdc8a9c52616c3f795f806f6486ca5b6ab374:GfSF3dFADekjVpe2X5kqUJApJdyRM5F1pXsZsCnb7V1TltF67P9T3ehKnKsf0C44ZqNaq/4Abf8X3RI4F9THhQ==:1000:g2ZaEZ5vMciZPd6TiLoN+6vqo90T0z99y1WZBReVEcCTvzpvG7q8dH6WNUBuYXTISK/uoWhNv6mee47HEviBqA/Eah9c4dDaIm4TlzCJrs/r1uAdPyZzaareVqexTDCCK2O5J4NjzAmNuapnC9riPMgmLba/sWWPbN7umMytLmVtftEQ3A3PdiYxUr4JFIWU08mBACuUbZwJ0YorhkiT/w==; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Apr+07+2023+15%3A03%3A27+GMT%2B0530+(India+Standard+Time)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=ed47391f-87ca-4abc-bb92-a8fb51165261&interactionCount=3&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0005%3A1%2CC0004%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=DE%3B; _gat=1; forterToken=0a3296a83bfe4bf28dfe113a22083781_1680860007259_1167_UDF43-m4_13ck; QuantumMetricSessionID=ccb4780cf3ea80e4ba7a46f044f0881b; lastRskxRun=1680860012656; _pxde=451d803c27bcd89845d2137ba7717f7fdde5102e9218e49335a96c142ec836ba:eyJ0aW1lc3RhbXAiOjE2ODA4NjAwMTAwMjUsImZfa2IiOjB9; IR_9060=1680860011948%7C0%7C1680860011948%7C%7C; IR_PI=8de5d8eb-d47b-11ed-a1f6-b5074c358207%7C1680946411948; _dd_s=rum=0&expire=1680860918021; _uetsid=91275390d47b11ed8677032edd179f9a; _uetvid=9127d8f0d47b11edafda871ad5a39be7',
        'origin': 'https://stockx.com',
        'referer': 'https://stockx.com/sneakers/most-popular?page=1',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'selected-country': 'IN',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-operation-name': 'Browse',
        'x-stockx-device-id': 'bc75ea53-9db9-4758-9657-8d68d423894e',
        'x-stockx-session-id': 'cb0e3be8-852d-4010-972b-c2440573f85d',
    }

    headers['referer'] = 'https://stockx.com/sneakers/most-popular?page={}'.format(i)
    # print(headers)
    data = '{"query":"query Browse($category: String, $filters: [BrowseFilterInput], $filtersVersion: Int, $query: String, $sort: BrowseSortInput, $page: BrowsePageInput, $currency: CurrencyCode, $country: String!, $market: String, $staticRanking: BrowseExperimentStaticRankingInput, $skipFavorite: Boolean!) {\\n  browse(\\n    category: $category\\n    filters: $filters\\n    filtersVersion: $filtersVersion\\n    query: $query\\n    sort: $sort\\n    page: $page\\n    experiments: {staticRanking: $staticRanking}\\n  ) {\\n    suggestions {\\n      isCuratedPage\\n      relatedPages {\\n        title\\n        url\\n      }\\n      locales\\n    }\\n    results {\\n      edges {\\n        objectId\\n        node {\\n          ... on Product {\\n            ...BrowseProductDetailsFragment\\n            ...FavoriteProductFragment @skip(if: $skipFavorite)\\n            ...ProductTraitsFragment\\n            ...FavoriteVariantsFragment @skip(if: $skipFavorite)\\n            market(currencyCode: $currency) {\\n              ...MarketFragment\\n            }\\n          }\\n          ... on Variant {\\n            id\\n            ...FavoriteVariantFragment @skip(if: $skipFavorite)\\n            product {\\n              ...BrowseProductDetailsFragment\\n              ...FavoriteProductFragment @skip(if: $skipFavorite)\\n              ...FavoriteVariantsFragment @skip(if: $skipFavorite)\\n              traits(filterTypes: [RELEASE_DATE, RETAIL_PRICE]) {\\n                name\\n                value\\n              }\\n            }\\n            market(currencyCode: $currency) {\\n              ...MarketFragment\\n            }\\n            traits {\\n              size\\n            }\\n          }\\n        }\\n      }\\n      pageInfo {\\n        limit\\n        page\\n        pageCount\\n        queryId\\n        queryIndex\\n        total\\n      }\\n    }\\n    query\\n  }\\n}\\n\\nfragment FavoriteProductFragment on Product {\\n  favorite\\n}\\n\\nfragment FavoriteVariantFragment on Variant {\\n  favorite\\n}\\n\\nfragment FavoriteVariantsFragment on Product {\\n  variants {\\n    id\\n    favorite\\n    traits {\\n      size\\n    }\\n  }\\n}\\n\\nfragment ProductTraitsFragment on Product {\\n  productTraits: traits(filterTypes: [RELEASE_DATE, RETAIL_PRICE]) {\\n    name\\n    value\\n  }\\n}\\n\\nfragment MarketFragment on Market {\\n  currencyCode\\n  bidAskData(market: $market, country: $country) {\\n    lowestAsk\\n    highestBid\\n    lastHighestBidTime\\n    lastLowestAskTime\\n  }\\n  state(country: $country) {\\n    numberOfCustodialAsks\\n  }\\n  salesInformation {\\n    lastSale\\n    lastSaleDate\\n    salesThisPeriod\\n    salesLastPeriod\\n    changeValue\\n    changePercentage\\n    volatility\\n    pricePremium\\n  }\\n  deadStock {\\n    sold\\n    averagePrice\\n  }\\n  statistics {\\n    last90Days {\\n      averagePrice\\n    }\\n  }\\n}\\n\\nfragment BrowseProductDetailsFragment on Product {\\n  id\\n  name\\n  urlKey\\n  title\\n  brand\\n  description\\n  model\\n  condition\\n  productCategory\\n  listingType\\n  media {\\n    thumbUrl\\n    smallImageUrl\\n  }\\n}","variables":{"query":"","category":"sneakers","filters":[{"id":"browseVerticals","selectedValues":["sneakers"]}],"filtersVersion":4,"sort":{"id":"most-active","order":"DESC"},"page":{"index":'+str(i)+',"limit":40},"currency":"USD","country":"IN","marketName":null,"skipFavorite":true,"staticRanking":{"enabled":false}},"operationName":"Browse"}'

    # print(data)
    #
    client = ScrapingBeeClient(api_key='BVSRQGL8H43UFWB2YEA5NH4OMYN34GS2H2QAJH566G9B0OTW0L4TTCW4OUSX0Y03J640WDG2LQRTQNGS')
    response = client.post('https://stockx.com/api/p/e',
                             headers=headers,
                             data=data,
                             params={

                                # "url":"https://stockx.com/sneakers/most-popular?page=2",
                                # "api_key":"BVSRQGL8H43UFWB2YEA5NH4OMYN34GS2H2QAJH566G9B0OTW0L4TTCW4OUSX0Y03J640WDG2LQRTQNGS",
                                'country_code': 'us',
                                'wait_browser': 'load',
                                'wait': '20000',
                                'timeout': '20000',
                                # 'premium_proxy': 'True'

                              }

    #
    #
    )
    #

    print(response.status_code)

    prd_data = json.loads(response.text)
    count = prd_data['data']['browse']['results']['edges']
    rank_on_pg = 0
    print(pg_no)
    for i in range(0,len(count)):
        rank_on_pg += 1
        sr_no += 1


        try:
            prd_id = prd_data['data']['browse']['results']['edges'][i]['node']['id']
        except:
            prd_id = ''

        try:
            prd_col = prd_data['data']['browse']['results']['edges'][i]['node']['name']
        except:
            prd_col = ''

        try:
            prd_url = 'https://stockx.com/' + prd_data['data']['browse']['results']['edges'][i]['node']['urlKey']
        except:
            prd_url = ''

        try:
            prd_name = prd_data['data']['browse']['results']['edges'][i]['node']['title']
        except:
            prd_name = ''


        try:
            prd_brand = prd_data['data']['browse']['results']['edges'][i]['node']['brand']
        except:
            prd_brand = ''

        try:
            prd_desc = prd_data['data']['browse']['results']['edges'][i]['node']['description']
        except:
            prd_desc = ''

        try:
            prd_model = prd_data['data']['browse']['results']['edges'][i]['node']['model']
        except:
            prd_model = ''

        try:
            prd_cond = prd_data['data']['browse']['results']['edges'][i]['node']['condition']
        except:
            prd_cond = ''

        try:
            prd_type = prd_data['data']['browse']['results']['edges'][i]['node']['productCategory']
        except:
            prd_type = ''

        try:
            prd_list_type = prd_data['data']['browse']['results']['edges'][i]['node']['listingType']
        except:
            prd_list_type = ''

        try:
            prd_img_url = prd_data['data']['browse']['results']['edges'][i]['node']['media']['smallImageUrl']
        except:
            prd_img_url = ''

        try:
            prd_retail_price = prd_data['data']['browse']['results']['edges'][i]['node']['productTraits'][0]['value']
        except:
            prd_retail_price = ''

        try:
            prd_release_date = prd_data['data']['browse']['results']['edges'][i]['node']['productTraits'][1]['value']
        except:
            prd_release_date = ''

        try:
            prd_curr_code = prd_data['data']['browse']['results']['edges'][i]['node']['market']['currencyCode']
        except:
            prd_curr_code = ''

        try:
            prd_low_ask = prd_data['data']['browse']['results']['edges'][i]['node']['market']['bidAskData']['lowestAsk']
        except:
            prd_low_ask = ''

        try:
            prd_lst_high_bid_tm = prd_data['data']['browse']['results']['edges'][i]['node']['market']['bidAskData']['lastHighestBidTime']
        except:
            prd_lst_high_bid_tm = ''

        try:
            prd_lst_low_ask_tm = prd_data['data']['browse']['results']['edges'][i]['node']['market']['bidAskData']['lastLowestAskTime']
        except:
            prd_lst_low_ask_tm = ''

        try:
            prd_last_sale = prd_data['data']['browse']['results']['edges'][i]['node']['market']['salesInformation']['lastSale']
        except:
            prd_last_sale  = ''

        try:
            prd_last_sale_dt = prd_data['data']['browse']['results']['edges'][i]['node']['market']['salesInformation']['lastSaleDate']
        except:
            prd_last_sale_dt  = ''

        try:
            prd_this_prd_sale = prd_data['data']['browse']['results']['edges'][i]['node']['market']['salesInformation']['salesThisPeriod']
        except:
            prd_this_prd_sale  = ''

        try:
            prd_last_prd_sale = prd_data['data']['browse']['results']['edges'][i]['node']['market']['salesInformation']['salesLastPeriod']
        except:
            prd_last_prd_sale  = ''

        try:
            prd_change_value = prd_data['data']['browse']['results']['edges'][i]['node']['market']['salesInformation']['changeValue']
        except:
            prd_change_value  = ''

        try:
            prd_change_per = prd_data['data']['browse']['results']['edges'][i]['node']['market']['salesInformation']['changePercentage']
        except:
            prd_change_per = ''

        try:
            prd_voltality = prd_data['data']['browse']['results']['edges'][i]['node']['market']['salesInformation']['volatility']
        except:
            prd_voltality = ''

        try:
            prd_price_prem = prd_data['data']['browse']['results']['edges'][i]['node']['market']['salesInformation']['pricePremium']
        except:
            prd_price_prem = ''

        try:
            prd_sold = prd_data['data']['browse']['results']['edges'][i]['node']['market']['deadStock']['sold']
        except:
            prd_sold = ''

        try:
            prd_avg_price = prd_data['data']['browse']['results']['edges'][i]['node']['market']['deadStock']['averagePrice']
        except:
            prd_avg_price = ''

        try:
            prd_lst90_avg_price = prd_data['data']['browse']['results']['edges'][i]['node']['market']['statistics']['last90Days']['averagePrice']
        except:
            prd_lst90_avg_price = ''

        try:
            curr_datetime = datetime.datetime.now()
            crawl_datetime = curr_datetime.strftime("%Y-%m-%d %I:%M:%S %p")
        except:
            crawl_datetime = ''

        try:
            with open('stockx_page_prd.csv', 'a', newline='', encoding='UTF-8') as fp:
                writer = csv.writer(fp)
                writer.writerow([

                    sr_no,
                    pg_no,
                    rank_on_pg,
                    prd_name,
                    prd_brand,
                    prd_col,
                    prd_id,
                    prd_url,
                    prd_model,
                    prd_cond,
                    prd_type,
                    prd_list_type,
                    prd_retail_price,
                    prd_curr_code,
                    prd_release_date,
                    prd_low_ask,
                    prd_lst_high_bid_tm,
                    prd_lst_low_ask_tm,
                    prd_last_sale,
                    prd_last_sale_dt,
                    prd_this_prd_sale,
                    prd_change_value,
                    prd_change_per,
                    prd_voltality,
                    prd_price_prem,
                    prd_sold,
                    prd_avg_price,
                    prd_lst90_avg_price,
                    prd_desc,
                    prd_img_url,
                    crawl_datetime




                ])
        except:
            pass


