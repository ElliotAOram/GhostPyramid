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
 * Created by Elliot on 11/03/2017.
 */
public class ActorLandingTest {

    @Rule
    public ActivityTestRule mActivityRule = new ActivityTestRule<>(ActorLanding.class);

    @Test
    public void testExpectedTextOnActivity() throws Exception {
        onView(withId(R.id.textview_actor_splash_welcome)).
                check(matches(withText("Welcome Actor")));
        onView(withId(R.id.textview_actor_splash_instructions)).
                check(matches(withText("As the Actor you will be given the choice between 5" +
                                       " different phrases. Once you select a phrase you will then"+
                                       " choose a word from the phrase to act out. You will be"+
                                       " asked to select a new word from the phrase if it guessed"+
                                       " correctly or the time for the round expires. The round" +
                                       " ends when the whole phrase has been guessed or the time" +
                                       " has expired.")));
        onView(withId(R.id.button_to_phrase_selection)).
                check(matches(withText("Continue to phrase selection")));
    }

}