package edu.upenn.cit594.processor;

import java.util.Map;

import edu.upenn.cit594.datamanagement.PopulationReader;
import edu.upenn.cit594.datamanagement.PropertyReader;
import edu.upenn.cit594.datamanagement.violationReader;
//

public class Processor {
	
	protected PropertyReader property_reader;
	protected PopulationReader population_reader;
	protected violationReader  violation_reader;
	
	protected TotalPopulation total_population;
	protected TotalFinePerCapita total_fine_per_capita;
	protected HouseAverageCalculator house_average_calculator;
	protected TotalMarketValuePerCapita  total_market_value_per_capita;
	protected FinePerCapitaTimesNumberOfHouses fine_per_capita_times_number_houses;
	
	
	public Processor( PropertyReader property_reader , PopulationReader population_reader, violationReader  violation_reader ) {
		
		this.property_reader = property_reader;
		this.population_reader = population_reader;
		this.violation_reader = violation_reader;
		
		this.total_population = new TotalPopulation(population_reader);
		this.total_fine_per_capita = new  TotalFinePerCapita( population_reader , violation_reader);
		this.house_average_calculator = new HouseAverageCalculator(property_reader);
		this.total_market_value_per_capita = new TotalMarketValuePerCapita ( population_reader , property_reader) ;
		this.fine_per_capita_times_number_houses = new FinePerCapitaTimesNumberOfHouses(property_reader , this.total_fine_per_capita);
	}
	
	
	// #1 - Total Population for All ZIP Codes
	
	public int getTotalPopulation() {
		
		return  this.total_population.calculateTotalPopulation();
	}
	
	// #2 Total Fines Per Capita
	public Map<Integer, Double> getTotalFinePerCapita() {
		return this.total_fine_per_capita.CalculateTotalFinePerCapita();
	}
	
	
//	#3  Average Market Value
	
	public int getAverageMarketValue(int zip) {
		return this.house_average_calculator.calculateAvergaeMarketValue(zip);
	}
	
	
//	#4  Average Total Livable Area
	
	public int getAverageLivableArea(int zip) {
		return this.house_average_calculator.calculateAvergaeLivableArea(zip);
	}
	
//	#5 Total Residential Market Value Per Capita
	
	public int getTotalResidentialMarketValuePerCapita (int zip) {
		return this.total_market_value_per_capita.CalculateTotalMarketValuePerCapita(zip);
	}
	
//	#6
	
	public double getFinePerCapitaTimesNumberOfHouses(int zip) {
		return this.fine_per_capita_times_number_houses.calculateFinePerCapitaTimesNumberOfHouses(zip);
	}
}
