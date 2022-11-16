package edu.upenn.cit594.ui;

import java.io.IOException;
import java.util.Map;
import java.util.Scanner;

import edu.upenn.cit594.logging.Logger;
import edu.upenn.cit594.processor.Processor;

public class UserInterface {

	protected Processor processor;
	protected Logger logger;
	protected Scanner in;
	
	protected String fileType;
	protected String parkingFileString;
	protected String propertiesFileString;
	protected String populationFileString;
	protected String logFileName;


	public UserInterface(Processor processor, String[] args) {
		
		this.fileType = args[0];
		this.parkingFileString = args[1];
		this.propertiesFileString = args[2];
		this.populationFileString = args[3];
		this.logFileName = args[4];
		
		
		this.processor = processor;
		logger = Logger.getInstance(logFileName);
		in = new Scanner(System.in);
		
		this.write_files();
		
	}

	public void start() throws IOException {


		System.out.print("Welcome to MCIT594 Group Project 102.");
		

		while (runLoop());

		in.close();
		logger.closePrintWriter();

	}

	public void setProcessor(Processor processor) {
		this.processor = processor;
	}

	protected boolean runLoop() throws IOException {
		printPromt();
		// initialize variables
		int choice = -1;
		int zipCode = -1;

		if ((choice = readChoice()) == -1) {
			System.out.println("Invalid choice: program exited");
			return false;
		}
		// log the choice
		logger.log(String.valueOf(System.currentTimeMillis()) + " " + choice + " ");

		if (choice == 0) {
			System.out.println("Program Exited");
			
			return false;

		} else if (choice == 1) {
			totalPopulation();
			return true;
		} else if (choice == 2) {
			parkingFines();
			return true;
		}

		// get zipcode
		System.out.println("Please Enter a ZIP Code: ");

		if ((zipCode = readZIPCode()) == -1) {
			System.out.println("Invalid ZIP Code: program exited");
			return false;
		}
		// log the zipcode
		logger.log(String.valueOf(System.currentTimeMillis()) + " " + zipCode + " ");

		if (choice == 3) {

			averageMarketValue(zipCode);
		} else if (choice == 4) {

			averageLivableArea(zipCode);
		} else if (choice == 5) {

			totalMarketValue(zipCode);
		} else if (choice == 6) {

			finePerCapitaTimesNumberOfHouses(zipCode);
		}

		return true;
	}

	protected void printPromt() {
		System.out.print("Please enter a number from 0-6 corresponding to the options listed:\n"
				+ "Please enter '0' to exit the program\n"
				+ "Please enter '1' to view the total population for all ZIP Codes\n"
				+ "Please enter '2' to view the total parking fines per captia for each ZIP Code\n"
				+ "Please enter '3' to view the average market value for residences in a specefied ZIP Code\n"
				+ "Please enter '4' to view the average total livable area for residences in a specified ZIP Code\n"
				+ "Please enter '5' to view the total residential market value per capita for a specified ZIP code\n"
				+ "Please enter '6' to view the fine per capita times the number of houses in a specified ZIP Code\n");
	}

	protected int readChoice() {
		// if there is an string, parse, make sure its between 0 - 6 return it
		int choice = -1;
		String input = in.nextLine();
		if (input.length() > 1) {
			return -1;
		} else {
			try {
				choice = Integer.parseInt(input);
			} catch (Exception e) {
				return -1;
			}
		}
		if (choice < 0 || choice > 6) {
			return -1;
		}
		return choice;
	}

	protected int readZIPCode() {
		// if there is an string, parse, make sure its between 10000-99999 return it
		int zipCode = -1;
		String input = in.nextLine();
		if (input.length() != 5) {
			return -1;
		} else {
			try {
				zipCode = Integer.parseInt(input);
			} catch (Exception e) {
				return -1;
			}
		}
		if (zipCode < 10000 || zipCode > 99999) {
			return -1;
		}
		return zipCode;
	}
	
	// 
	public void write_files() {
		// log start up time and arguments passed
		logger.log(String.valueOf(System.currentTimeMillis()) + " " + fileType + " " + parkingFileString + " "
				+ propertiesFileString + " " + populationFileString + " " + logFileName + " ");
		
	}

	// ---------------PART 1 SOLUTION-----------------
	protected void totalPopulation() {

		System.out.println(processor.getTotalPopulation());

	}

	// ---------------PART 2 SOLUTION-----------------
	protected void parkingFines() {
		Map<Integer, Double> FinePerCapita = processor.getTotalFinePerCapita();
		for (Integer zip : FinePerCapita.keySet()) {
			System.out.println(zip + " " +  String.format("%.4f",  FinePerCapita.get(zip) )  );
		}
	}

	// ---------------PART 3 SOLUTION-----------------
	protected void averageMarketValue(int zipCode) {
		System.out.println(processor.getAverageMarketValue(zipCode));
	}

	// ---------------PART 4 SOLUTION-----------------
	protected void averageLivableArea(int zipCode) {
		System.out.println(processor.getAverageLivableArea(zipCode));
	}

	// ---------------PART 5 SOLUTION-----------------
	protected void totalMarketValue(int zipCode) {
		System.out.println(processor.getTotalResidentialMarketValuePerCapita(zipCode));
	}

	// ---------------PART 6 SOLUTION-----------------
	protected void finePerCapitaTimesNumberOfHouses(int zipCode) {
		System.out.println( processor.getFinePerCapitaTimesNumberOfHouses(zipCode));
	}

}
