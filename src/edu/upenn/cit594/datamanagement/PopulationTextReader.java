package edu.upenn.cit594.datamanagement;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import edu.upenn.cit594.logging.Logger;


public class PopulationTextReader implements PopulationReader {
	
	protected String filename;
	protected String logFileName;
	Map<Integer, Integer> population;

	public PopulationTextReader(String filename , String logFileName) {
		this.filename = filename;
		this.population = new HashMap<Integer, Integer>();
		this.logFileName = logFileName;
		
		this.getPopulationData();
	}


	private void getPopulationData() {
		// TODO Auto-generated method stub
		
		
		
		//create file object
		File file = new File(filename);

		//define file reader
		FileReader fileReader = null;

		//define buffered reader
		BufferedReader bufferedReader = null;

		try {
			fileReader = new FileReader(file);
			bufferedReader = new BufferedReader(fileReader);
			
			Logger l = Logger.getInstance(logFileName);
			l.log(String.valueOf(System.currentTimeMillis()) + " " + this.filename );
			
			String line;

			while ((line = bufferedReader.readLine()) != null) {

				try {

					String[] str= line.trim().split("\\s");
					int zip = Integer.parseInt(str[0]);
					int population = Integer.parseInt(str[1]);
					this.population.put(zip, population);


				} catch(Exception e) {
				}

			}
		} catch (FileNotFoundException e) {
			//gets and prints filename
			System.out.println("Sorry, " + file.getName() + " not found.");
		}catch (IOException e) {
			//prints the error message and info about which line
			e.printStackTrace();
		}finally {

			//regardless, close file objects
			try {
				fileReader.close();
				bufferedReader.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

		
		

	}

/**
 * 
 * @return
 */
	@Override
	public Map<Integer, Integer> getPopulation() {
		return population;
	}

}
