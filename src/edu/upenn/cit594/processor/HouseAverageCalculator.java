package edu.upenn.cit594.processor;

import java.util.HashMap;
import java.util.Map;

import edu.upenn.cit594.data.House;
import edu.upenn.cit594.datamanagement.PropertyReader;

public class HouseAverageCalculator {

	private PropertyReader property_reader;
	Map<Integer, Integer> AvergaeMarketValueMap;
	Map<Integer, Integer> AverageLivableAreaMap;

	public HouseAverageCalculator( PropertyReader property_reader ) {
		this.property_reader = property_reader;
		AvergaeMarketValueMap = new HashMap<Integer, Integer>();
		AverageLivableAreaMap = new HashMap<Integer, Integer>();
	}


	public double calculateAverage(int zip, HouseAverage house_avergae) {

		double average=0;
		int count=0;
		double total_value = 0;

		for(House house: property_reader.getProperties() ) {
			double house_value =  house_avergae.getHouseMetric(zip, house);
			if (house_value>0 ) {
				total_value += house_value;
				count+=1;
			}
		}
		
		if (count>0) {
			average = total_value/count;
		}
		return average;
	}
	
	
	public int calculateAvergaeMarketValue (int zip ) {
		
		if (AvergaeMarketValueMap.containsKey(zip)) {
			return(AvergaeMarketValueMap.get(zip) );
		}else {
			double average = calculateAverage( zip, new AverageMarketValue()) ;
			AvergaeMarketValueMap.put(zip,  (int)Math.floor(average)   );
			return  (int)Math.floor(average);
		}
		
	}
	
	
	public int calculateAvergaeLivableArea (int zip ) {
		
		if (AverageLivableAreaMap.containsKey(zip)) {
			return(AverageLivableAreaMap.get(zip) );
		}else {
			double average = calculateAverage( zip, new AverageLivableArea()) ;
			AverageLivableAreaMap.put(zip, (int)Math.floor(average)    );
			return (int)Math.floor(average) ;
		}
		
	}


}
