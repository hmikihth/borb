# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters
(such as in a computer program or web page) into a sequence of tokens (strings with an assigned and thus identified meaning).
A program that performs lexical analysis may be termed a lexer, tokenizer, or scanner,
although scanner is also a term for the first stage of a lexer.
A lexer is generally combined with a parser, which together analyze the syntax of programming languages, web pages,
and so forth.
"""
import typing

from borb.pdf.canvas.layout.equation.token import Token, TokenType


class Tokenizer:
    """
    In computer science, lexical analysis, lexing or tokenization is the process of converting a sequence of characters
    (such as in a computer program or web page) into a sequence of tokens (strings with an assigned and thus identified meaning).
    A program that performs lexical analysis may be termed a lexer, tokenizer, or scanner,
    although scanner is also a term for the first stage of a lexer.
    A lexer is generally combined with a parser, which together analyze the syntax of programming languages, web pages,
    and so forth.
    """

    @staticmethod
    def tokenize(infix_expression: str) -> typing.List[Token]:
        """
        This function converts an infix expression to a typing.List[Token]
        :param infix_expression:    the infix expression (as str) to tokenize
        :return:                    the typing.List[Token] representing the tokenized output
        """
        # variable to store output
        output: typing.List[Token] = []

        # process expression
        i: int = 0
        while i < len(infix_expression):

            #
            # SPACE
            #
            if infix_expression[i] == " ":
                i += 1
                continue

            #
            # PARENTHESES
            #

            if infix_expression[i] == "(":
                output += [Token(text="(", type=TokenType.LEFT_PARENTHESIS)]
                i += 1
                continue
            if infix_expression[i] == ")":
                output += [Token(text=")", type=TokenType.RIGHT_PARENTHESIS)]
                i += 1
                continue

            #
            # BASIC OPERATORS
            #

            if infix_expression[i] == "±":
                output += [
                    Token(
                        text="±",
                        type=TokenType.OPERATOR,
                        precedence=2,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 1
                continue
            if infix_expression[i] == "+":
                output += [
                    Token(
                        text="+",
                        type=TokenType.OPERATOR,
                        precedence=2,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 1
                continue
            if infix_expression[i] == "-":
                output += [
                    Token(
                        text="-",
                        type=TokenType.OPERATOR,
                        precedence=2,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 1
                continue
            if infix_expression[i] == "*":
                output += [
                    Token(
                        text="*",
                        type=TokenType.OPERATOR,
                        precedence=3,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 1
                continue
            if infix_expression[i] == "/":
                output += [
                    Token(
                        text="/",
                        type=TokenType.OPERATOR,
                        precedence=3,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 1
                continue

            #
            # COMPARISON
            #

            if infix_expression[i:].startswith("!="):
                output += [
                    Token(
                        text="≠",
                        type=TokenType.OPERATOR,
                        precedence=1,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 2
                continue

            if infix_expression[i:].startswith(">="):
                output += [
                    Token(
                        text="≥",
                        type=TokenType.OPERATOR,
                        precedence=1,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 2
                continue

            if infix_expression[i:].startswith("<="):
                output += [
                    Token(
                        text="≤",
                        type=TokenType.OPERATOR,
                        precedence=1,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 2
                continue

            if infix_expression[i] == ">":
                output += [
                    Token(
                        text=">",
                        type=TokenType.OPERATOR,
                        precedence=1,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 1
                continue

            if infix_expression[i] == "<":
                output += [
                    Token(
                        text="<",
                        type=TokenType.OPERATOR,
                        precedence=1,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 1
                continue

            if infix_expression[i] == "=":
                output += [
                    Token(
                        text="=",
                        type=TokenType.OPERATOR,
                        precedence=1,
                        is_left_associative=True,
                        number_of_arguments=2,
                    )
                ]
                i += 1
                continue

            #
            # POWERS
            #

            if infix_expression[i] == "^":
                output += [
                    Token(
                        text="^",
                        type=TokenType.OPERATOR,
                        precedence=4,
                        is_left_associative=False,
                        number_of_arguments=2,
                    )
                ]
                i += 1
                continue
            if infix_expression[i] == "²":
                output += [
                    Token(
                        text="^",
                        type=TokenType.OPERATOR,
                        precedence=4,
                        is_left_associative=False,
                        number_of_arguments=2,
                    )
                ]
                output += [Token(text="2", type=TokenType.NUMBER)]
                i += 1
                continue
            if infix_expression[i] == "³":
                output += [
                    Token(
                        text="^",
                        type=TokenType.OPERATOR,
                        precedence=4,
                        is_left_associative=False,
                        number_of_arguments=2,
                    )
                ]
                output += [Token(text="3", type=TokenType.NUMBER)]
                i += 1
                continue
            if infix_expression[i:].startswith("sqrt"):
                output += [
                    Token(
                        text="sqrt",
                        type=TokenType.FUNCTION,
                        precedence=4,
                        is_left_associative=False,
                        number_of_arguments=1,
                    )
                ]
                i += 4
                continue
            #
            # TRIG FUNCTIONS
            #

            if infix_expression[i:].startswith("sin"):
                output += [
                    Token(text="sin", type=TokenType.FUNCTION, number_of_arguments=1)
                ]
                i += 3
                continue
            if infix_expression[i:].startswith("cos"):
                output += [
                    Token(text="cos", type=TokenType.FUNCTION, number_of_arguments=1)
                ]
                i += 3
                continue
            if infix_expression[i:].startswith("tan"):
                output += [
                    Token(text="tan", type=TokenType.FUNCTION, number_of_arguments=1)
                ]
                i += 3
                continue
            if infix_expression[i:].startswith("cot"):
                output += [
                    Token(text="cot", type=TokenType.FUNCTION, number_of_arguments=1)
                ]
                i += 3
                continue
            if infix_expression[i:].startswith("sec"):
                output += [
                    Token(text="sec", type=TokenType.FUNCTION, number_of_arguments=1)
                ]
                i += 3
                continue
            if infix_expression[i:].startswith("csc"):
                output += [
                    Token(text="csc", type=TokenType.FUNCTION, number_of_arguments=1)
                ]
                i += 3
                continue

            #
            # ABS
            #

            if infix_expression[i:].startswith("abs"):
                output += [
                    Token(text="abs", type=TokenType.FUNCTION, number_of_arguments=1)
                ]
                i += 3
                continue

            #
            # NUMBERS
            #

            if infix_expression[i] in "0123456789.":
                j: int = i
                while (
                    j < len(infix_expression) and infix_expression[j] in "0123456789."
                ):
                    j += 1
                output += [Token(text=infix_expression[i:j], type=TokenType.NUMBER)]
                i = j
                continue

            # IF the token can not be interpreted as anything else
            # AND the previous token was a VARIABLE
            # THEN concatenate the token to the previous VARIABLE
            if len(output) > 0 and output[-1]._type == TokenType.VARIABLE:
                output[-1]._text += infix_expression[i]
                i += 1
                continue

            # IF the token can not be interpreted as anything else
            # AND there is no previous token
            # THEN mark the token as a variable
            output += [Token(text=infix_expression[i], type=TokenType.VARIABLE)]
            i += 1

        # fix unary minus
        for i, t in enumerate(output):
            if output[i].get_type() != TokenType.OPERATOR:
                continue
            if output[i].get_text() != "-":
                continue
            if (
                i == 0
                or output[i - 1].get_type() == TokenType.OPERATOR
                or output[i - 1].get_type() == TokenType.LEFT_PARENTHESIS
            ):
                output[i]._number_of_arguments = 1
                output[i]._precedence = 5
                continue

        # return
        return output
