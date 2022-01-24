package com.test.zelando;
/*
 * @created 1/23/2022 - 6:01 PM
 * @project code_challenge
 * @author adel.ramezani (adramazany@gmail.com)
 */

import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

public class Task2 {
    Logger logger = LoggerFactory.getLogger(Task2.class);

    @Test
    void test_task2() {
        String s1 = "CBACD";
        String s2 = "CABABD";

        assertThat(solution(s1)).isEqualTo("C");
        assertThat(solution(s2)).isEqualTo("");
    }

    public String solution(String S) {
        // write your code in Java SE 8
        logger.debug("solution: {}", S);

        StringBuilder sb = new StringBuilder();
        boolean is_last_deleted = false;
        for (int i = 0; i < S.length(); i++) {
            is_last_deleted = false;
            if (i == S.length() - 1) {
                sb.append(S.charAt(S.length() - 1));
            } else if (i < S.length() && !(
                    (S.charAt(i) == 'A' && S.charAt(i + 1) == 'B')
                            || (S.charAt(i) == 'B' && S.charAt(i + 1) == 'A')
                            || (S.charAt(i) == 'C' && S.charAt(i + 1) == 'D')
                            || (S.charAt(i) == 'D' && S.charAt(i + 1) == 'C')
            )) {
                sb.append(S.charAt(i));
            } else {
                i++;
            }
        }
        logger.debug("sb: {}", sb.toString());

        if (sb.length() < S.length()) {
            return solution(sb.toString());
        }

        return sb.toString();
    }
}
