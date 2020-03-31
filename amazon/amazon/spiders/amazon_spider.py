
import scrapy

from ..items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = ['https://www.amazon.in/s?bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&fst=as%3Aoff&qid=1585658099&rnid=2684818031&ref=lp_976389031_nr_p_n_publication_date_0']

    def parse(self, response):
        items = AmazonItem()

        product_name = response.css('.s-line-clamp-2::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base::text').extract()

        product_price = response.css('.index\=5 .a-price-whole , .index\=4 .a-price-whole , .a-spacing-mini .a-price-whole , .index\=10 .a-size-base , .index\=0 .a-color-secondary .a-link-normal::text').extract()

        product_imagelink = response.css('.s-image::attr(src)').extract()



        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink


        yield items


        next_page = 'https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&page='+str(AmazonSpiderSpider.page_number)+'&fst=as%3Aoff&qid=1585673810&rnid=2684818031&ref=sr_pg_2'

        if AmazonSpiderSpider.page_number <=100:
            AmazonSpiderSpider.page_number+=1
            yield response.follow(next_page, callback = self.parse)