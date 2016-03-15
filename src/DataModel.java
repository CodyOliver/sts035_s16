import javax.swing.JFrame;

import java.util.*;



public class DataModel implements Runnable{
	
//	JFrame frame;
	Renderer render;
	private List<Double> data = Arrays.asList(0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,
			11.0,10.0,9.0,8.0,7.0,6.0,5.0,4.0,3.0,2.0,1.0,0.0); 
	
	public DataModel(Renderer r){
//		this.frame = frame;
		this.render = r;
	}

	@Override
	public void run() {
					
		for(BallMover bm: render.artFrame.balls){
			
			double index = (double)render.artFrame.balls.indexOf(bm);
			double y = data.get((int) index).intValue();
			render.artFrame.moveBallTo((int)index,(int) y*10);
			System.out.println("y: "+String.valueOf(y));
				
			
		render.repaint();
			
		try {
			Thread.sleep(100);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		}
		
	}

}
