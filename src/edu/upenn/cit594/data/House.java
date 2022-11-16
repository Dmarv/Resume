package edu.upenn.cit594.data;

public class House {
	
	private String market_value;
	private String total_livable_area;
	private int zip_code;
	
	public House(String market_value, String total_livable_area, int zip_code) {
		this.market_value = market_value;
		this.total_livable_area = total_livable_area;
		this.zip_code = zip_code;
	}

	public String getMarket_value() {
		return market_value;
	}

	public String getTotal_livable_area() {
		return total_livable_area;
	}

	public int getZip_code() {
		return zip_code;
	}


	
	
	

}
