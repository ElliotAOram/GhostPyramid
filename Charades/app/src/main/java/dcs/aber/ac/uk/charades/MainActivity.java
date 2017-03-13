package dcs.aber.ac.uk.charades;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;


public class MainActivity extends BlankActivity{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    /**
     * Starts the intent to go to the actor splash.
     * Finish is called at the end of this page to ensure you can not return to this page.
     * @param view :: The current activity view
     */
    public void toActorSplash(View view) {
        Intent intent = new Intent(this, ActorLanding.class);
        startActivity(intent);
        finish();
    }

    /**
     * Starts the intent to go to the viewer splash.
     * Finish is called at the end of this page to ensure you can not return to this page.
     * @param view :: The current activity view
     */
    public void toViewerSplash(View view) {
        Intent intent = new Intent(this, ViewerLanding.class);
        startActivity(intent);
        finish();
    }


}
