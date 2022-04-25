import requests
from app.utils.utils import selector_from_response

def parse_stock(response, rows_limit):

    selector = selector_from_response(response)
    stock_data = []

    try:
        company_name = selector.xpath('//*[contains(@class, "D(ib) Fz(18px)")]//text()').extract_first()
        table_rows = selector.xpath('//div[@id="mrt-node-Col1-1-HistoricalDataTable"]//table//tbody/tr')
        if len(table_rows) > 0:
            for index, row in enumerate(table_rows):
                if index == rows_limit:
                    break
                data = {
                    "date": row.xpath('./td[1]//text()').extract_first(),
                    "open": row.xpath('./td[2]//text()').extract_first(),
                    "high": row.xpath('./td[3]//text()').extract_first(),
                    "low": row.xpath('./td[4]//text()').extract_first(),
                    "close": row.xpath('./td[5]//text()').extract_first(),
                    "adj_close": row.xpath('./td[6]//text()').extract_first(),
                    "volume": row.xpath('./td[7]//text()').extract_first()
                }

                stock_data.append(data)

            return {
                "company_name": company_name,
                "stock_history": stock_data
            }

        else:
            return None

    except Exception as e:
        return None

def extract_stock_history(stock_name, rows_limit):

    source = f'https://finance.yahoo.com/quote/{stock_name}/history?p={stock_name}'
    session = requests.Session()
    session.headers = {
        'Accept-Language': 'en-US',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) '
                      'Gecko/20100101 Firefox/60.0'
    }

    response = session.get(
        f'{source}',
        headers={'referer': '' + source + ''}
    )
    response.raise_for_status()
    data = parse_stock(response, rows_limit)

    if data:
        return data
    else:
        return None



