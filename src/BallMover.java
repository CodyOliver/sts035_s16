import java.awt.Color;


public class BallMover implements Runnable  {
	
	Ball ball;
	Frame frame;
	Renderer render;
	boolean selected = false;
	int goal;
	
	public BallMover(int d,int x,int y,int z,Color c, Frame f, Renderer r){
		ball = new Ball(d,x,y,z,c);
		this.render = r;
	}
	
	public void moveTo(int y){
		this.goal = y;
	}
	
	@Override
	public void run() {
		
		while(goal!=ball.y_pos){
			
			if(ball.y_pos>goal){
				ball.y_pos-=1;
			}else if(ball.y_pos<goal){
				ball.y_pos+=1;
			}
		
			render.repaint();
			
			try {
				Thread.sleep(20);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		
		
	}

}
