import javax.swing.JFrame;


public class SineWave implements Runnable{
	
//	JFrame frame;
	Renderer render;
	
	public SineWave(Renderer r){
//		this.frame = frame;
		this.render = r;
	}

	@Override
	public void run() {
		double count = 0;
		
		double num = (double)render.artFrame.balls.size();
		
		while(count<200){
			
			
			for(BallMover bm: render.artFrame.balls){
				double index = (double)render.artFrame.balls.indexOf(bm);
				double y =  Math.sin((index/num)*Math.PI+(count/10)*Math.PI);
				render.artFrame.moveBallTo((int)index, (int)(60+30*y));
				System.out.println("y: "+String.valueOf(y));
				
			}
			
			render.repaint();
			
			try {
				Thread.sleep(100);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			
			count+=1;
		}
		
	}

}
