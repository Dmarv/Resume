package edu.upenn.cit594.datamanagement;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import edu.upenn.cit594.data.House;
import edu.upenn.cit594.logging.Logger;

public class CSVPropertyReader implements PropertyReader {

	protected String filename;
	private List<House> properties;
	protected String logFileName;

	public CSVPropertyReader(String filename, String logFileName ) {
		this.filename = filename;
		this.properties = new ArrayList<House>();
		this.logFileName = logFileName;
		this.populateAllProperties();
	}


	private void populateAllProperties() {



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
			int index_market_value=0;
			int index_total_livable_area=0;
			int index_zip_code=0;

			// reading line titles:

			line = bufferedReader.readLine();
			String [] firstline= line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)");
			index_market_value= this.getIndex(firstline, "market_value");  //System.out.println(index_market_value);
			index_total_livable_area= this.getIndex(firstline, "total_livable_area");  //System.out.println(index_total_livable_area);
			index_zip_code= this.getIndex(firstline, "zip_code");  //System.out.println(index_zip_code);

			while ((line = bufferedReader.readLine()) != null) {

				try {

//										String [] str= line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)");
//										String market_value = str[index_market_value];
//										String total_livable_area= str[index_total_livable_area];
//										int zip_code = Integer.parseInt( str[index_zip_code].substring(0,5) ); 

					List<String> str =  SimpleCommaSeparation(line);
					String market_value = str.get(index_market_value);
					String total_livable_area= str.get(index_total_livable_area);
					int zip_code = Integer.parseInt( str.get(index_zip_code).substring(0,5) ); 

					House newHouse = new House(market_value , total_livable_area, zip_code );
					this.properties.add(newHouse);


				} catch(Exception e) {
					System.out.println(line);
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
	public int getIndex(String[] strArray, String str) {

		int Index = 0;

		for(String st:strArray) {
			//			System.out.println(Index + ":  "+ st);
			if(st.toUpperCase().equals(str.toUpperCase())) return Index;
			Index++;
		}

		return Index;

	}

	/**
	 * 
	 * @return
	 */
	@Override
	public List<House> getProperties() {
		return properties;
	}


	/**
	 * 
	 * @param str
	 * @return
	 */

	private List<String> SimpleCommaSeparation(String strin) {

		List<String> strout= new ArrayList<String>();

		String[] str = strin.split(",");
		String st="";
		boolean open= false;
		int index= 0;
		for (int i=0; i<str.length; i++) {


			if (charCount(str[i], '\"')%2==0 && !open) {
				strout.add(str[i]);
				st= "";
//				System.out.println(index + ": "+ str[i] );
				index++;
			}else {
				st += str[i];
				open= true;
				if (charCount(st, '\"')%2==0) {
					strout.add(st);
					open= false;
//					System.out.println(index + ": "+ st );
					index++;
				}
			}
		}

		return strout;
	}


	/**
	 * 
	 * @param str
	 * @param c
	 * @return
	 */
	private static int charCount( String str, char c) {
		int count = 0;
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == c) {
				count++;
			}
		}

		return count;
	}

	/**
	 * 
	 */

}
