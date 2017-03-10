package dcs.aber.ac.uk.charades;

import android.app.Instrumentation;
import android.support.test.rule.ActivityTestRule;
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
    public void testExpectedText() {
        onView(withId(R.id.textedit_select_role)).check(matches(withText("Select a role for this device")));
        onView(withId(R.id.button_to_actor_landing)).check(matches(withText("Actor")));
        onView(withId(R.id.button_to_viewer_landing)).check(matches(withText("Viewer")));
    }

    @Test
    public void toViewerSplash() throws Exception {
        // register next activity that need to be monitored.
        Instrumentation.ActivityMonitor activityMonitor = getInstrumentation().addMonitor(ViewerLanding.class.getName(), null, false);

        // open current activity.
        MainActivity myActivity = (MainActivity) mActivityRule.getActivity();
        final Button button = (Button) myActivity.findViewById(R.id.button_to_viewer_landing);
        myActivity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                // click button and open next activity.
                button.performClick();
            }
        });

        //Watch for the timeout
        //example values 5000 if in ms, or 5 if it's in seconds.
        ViewerLanding nextActivity = (ViewerLanding) getInstrumentation().waitForMonitorWithTimeout(activityMonitor, 5000);
        // next activity is opened and captured.
        assertNotNull(nextActivity);
        nextActivity .finish();
    }

    @Test
    public void toActorSplash() throws Exception {
        // register next activity that need to be monitored.
        Instrumentation.ActivityMonitor activityMonitor = getInstrumentation().addMonitor(ActorLanding.class.getName(), null, false);

        // open current activity.
        MainActivity myActivity = (MainActivity) mActivityRule.getActivity();
        final Button button = (Button) myActivity.findViewById(R.id.button_to_actor_landing);
        myActivity.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                // click button and open next activity.
                button.performClick();
            }
        });

        //Watch for the timeout
        //example values 5000 if in ms, or 5 if it's in seconds.
        ActorLanding nextActivity = (ActorLanding) getInstrumentation().waitForMonitorWithTimeout(activityMonitor, 5000);
        // next activity is opened and captured.
        assertNotNull(nextActivity);
        nextActivity .finish();
    }

}