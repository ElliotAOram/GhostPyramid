package dcs.aber.ac.uk.charades;

import android.support.test.rule.ActivityTestRule;

import org.junit.Rule;
import org.junit.Test;

import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.junit.Assert.*;

/**
 * Created by Elliot on 10/03/2017.
 */
public class ViewerLandingTest {

    @Rule
    public ActivityTestRule mActivityRule = new ActivityTestRule<>(ViewerLanding.class);

    @Test
    public void testExpectedTextOnActivity() throws Exception {
        onView(withId(R.id.textview_viewer_splash_welcome)).
                check(matches(withText("Welcome Viewer")));
        onView(withId(R.id.textview_viewer_splash_instructions)).
                check(matches(withText("As the Viewer you will be shown the topic of the phrase,"+
                                       " current word in the phrase, number of letters in the"+
                                       " phrase and the time remaining until the word is revealed."+
                                       " You must attempt to guess the word being acted by looking"+
                                       " at the hologram in front of you. The fast you guess,"+
                                       " the more points you get!")));
        onView(withId(R.id.textview_viewer_wait_for_prompt)).
                check(matches(withText("Please wait for the game to begin...")));
    }

}