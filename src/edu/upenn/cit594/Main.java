package edu.upenn.cit594;

import java.io.File;
import java.io.IOException;
import edu.upenn.cit594.datamanagement.CSVPropertyReader;
import edu.upenn.cit594.datamanagement.CsvViolationReader;
import edu.upenn.cit594.datamanagement.JsonViolationReader;
import edu.upenn.cit594.datamanagement.PopulationReader;
import edu.upenn.cit594.datamanagement.PopulationTextReader;
import edu.upenn.cit594.datamanagement.PropertyReader;
import edu.upenn.cit594.datamanagement.violationReader;
import edu.upenn.cit594.processor.Processor;
import edu.upenn.cit594.ui.UserInterface;

public class Main {

	public static void main(String[] args) throws IOException {
		// check for erros
		
		if (args.length != 5
				|| !((args[0].toLowerCase().contentEquals("json")) || (args[0].toLowerCase().contentEquals("csv")))
				|| !args[2].toLowerCase().contains(".csv") || !args[3].toLowerCase().contains(".txt")) {
			System.out.println("Error: arguments formated incorrectly");
			return;
		}

		// System.out.println("hello");
		// set args to easy to understand strings
		String fileType = args[0].toLowerCase();
		String parkingFileString = args[1];
		String propertiesFileString = args[2];
		String populationFileString = args[3];
		String logFileName = args[4];



		// set up files
		File parkingFile = new File(parkingFileString);
		File propertiesFile = new File(propertiesFileString);
		File populationFile = new File(populationFileString);

		if ((!parkingFile.canRead()) || (!propertiesFile.canRead()) || (!populationFile.canRead())) {
			System.out.println("Error: file cannont be either found or read");
			return;
		}

		// we used interfaces to future-proof the work
		Processor processor = null;
		UserInterface ui = new UserInterface(processor, args);
		
		
		PropertyReader property_reader = new CSVPropertyReader(propertiesFileString, logFileName);
		PopulationReader population_reader = new PopulationTextReader(populationFileString ,logFileName);

		if (fileType.contentEquals("json")) {
			violationReader vilation_reader = new JsonViolationReader(parkingFileString ,  logFileName);
			processor = new Processor(property_reader, population_reader, vilation_reader);

		}
		if (fileType.contentEquals("csv")) {
			violationReader vilation_reader = new CsvViolationReader(parkingFileString, logFileName);
			processor = new Processor(property_reader, population_reader, vilation_reader);
		}

		ui.setProcessor(processor);

		ui.start();

	}

}
