package edu.upenn.cit594.processor;

import edu.upenn.cit594.data.House;

public class AverageLivableArea implements HouseAverage{

	@Override
	public double getHouseMetric(int zip, House house) {
		// TODO Auto-generated method stub

		double value=0;
		if (zip== house.getZip_code()) {
			try {
				value = Double.parseDouble( house.getTotal_livable_area() );
			}catch(Exception e) {}
		}
		return value;

	}

}
