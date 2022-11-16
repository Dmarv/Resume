package edu.upenn.cit594.processor;

import edu.upenn.cit594.data.House;

public class AverageMarketValue implements HouseAverage {


	@Override
	public double getHouseMetric(int zip, House house) {

		double value=0;
		if (zip== house.getZip_code()) {
			try {
				value = Double.parseDouble( house.getMarket_value() );
			}catch(Exception e) {}
		}
		return value;
	}
	

}
