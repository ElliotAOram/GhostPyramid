package dcs.aber.ac.uk.charades;

import android.app.Instrumentation;
import android.support.test.rule.ActivityTestRule;
import android.support.v7.app.AppCompatActivity;
import android.widget.Button;

import org.junit.Rule;
import org.junit.Test;


import static android.support.test.InstrumentationRegistry.getInstrumentation;
import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.junit.Assert.*;

/**
 * Created by Elliot on 10/03/2017.
 */
public class MainActivityTest {

    @Rule
    public ActivityTestRule mActivityRule = new ActivityTestRule<>(MainActivity.class);


    @Test
    public void testExpectedTextOnActivity() {
        onView(withId(R.id.textedit_select_role)).check(matches(withText("Select a role for this device")));
        onView(withId(R.id.button_to_actor_landing)).check(matches(withText("Actor")));
        onView(withId(R.id.button_to_viewer_landing)).check(matches(withText("Viewer")));
    }

    private Instrumentation.ActivityMonitor transitionActivity(String className, int buttonId){
        // register next activity that need to be monitored.
        Instrumentation.ActivityMonitor activityMonitor = getInstrumentation().addMonitor(className, null, false);

        // open current activity.
        MainActivity myActivity = (MainActivity) mActivityRule.getActivity();
        final Button button = (Button) myActivity.findViewById(buttonId);
        myActivity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                // click button and open next activity.
                button.performClick();
            }
        });
        return activityMonitor;
    }


    @Test
    public void testTransitionToViewerSplash() throws Exception {
        Instrumentation.ActivityMonitor actMon =
                transitionActivity(ViewerLanding.class.getName(), R.id.button_to_viewer_landing);

        ViewerLanding nextActivity =
                (ViewerLanding) getInstrumentation().waitForMonitorWithTimeout(actMon, 5000);
        assertNotNull(nextActivity);
        nextActivity.finish();
    }

    @Test
    public void testTransitionToActorSplash() throws Exception {
        // register next activity that need to be monitored.
        Instrumentation.ActivityMonitor actMon =
                transitionActivity(ActorLanding.class.getName(), R.id.button_to_actor_landing);

        ActorLanding nextActivity =
                (ActorLanding) getInstrumentation().waitForMonitorWithTimeout(actMon, 5000);
        assertNotNull(nextActivity);
        nextActivity .finish();
    }

}