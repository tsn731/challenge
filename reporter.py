#!/usr/bin/env python
import json, pprint, numpy

def make_report(filename):
    with open(filename) as json_data:
        listings = json.load(json_data)
        # get list of unique cities
        cities = list(set(map(lambda item: item['city'], listings)))
        report = []
        # generate report for each city
        for c in cities:
            city_report = {}
            # filter data pertaining to a city
            tmplist = filter(lambda item: item['city'] == c, listings)

            # list of sale price
            sale_price = map(lambda item: item['sale_price'], tmplist)

            # total listings
            total_listings = len(tmplist)

            # average
            average = sum(sale_price) / total_listings

            # median
            median = numpy.median(numpy.array(sale_price))

            city_report["total_listings"] = len(tmplist)
            city_report["average_price"] = average
            city_report["median"] = median
            city_report["city"] = c
            report.append(city_report)

        # repeat for aggregate
        agg_sale_price = map(lambda item: item['sale_price'], listings)
        agg_total_listings = len(listings)
        agg_avg_price = sum(agg_sale_price)/total_listings
        agg_median = numpy.median(numpy.array(agg_sale_price))
        agg_report = {}
        agg_report["total_listings"] = agg_total_listings
        agg_report["average_price"] = agg_avg_price
        agg_report["median"] = agg_median
        agg_report["city"] = "Total"
        report.append( agg_report)
        return report

if __name__ == '__main__':
    pprint.pprint(make_report('sample_data.json'))
