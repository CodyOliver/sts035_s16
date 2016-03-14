import java.awt.Color;


public class Ball {
	
	int diameter = 20;
	int x_pos = 0;
	int y_pos = 0;
	int z_pos = 0;
	Color color = Color.LIGHT_GRAY;
	boolean selected = false;
	
	public Ball(int d,int x,int y,int z,Color c){
		this.x_pos = x;
		this.y_pos = y;
		this.color = c;

	}

}
