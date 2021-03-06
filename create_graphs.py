#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys as mod_sys
import os as mod_os
import random as mod_random

mod_sys.path.append('submodules/vcgraphtex')

import vcgraphtex as mod_graph

WHITE = (1, 1, 1)
RED = (1, 0, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)
GRAY = (.6, .6, .6)

def graph_primjer_s_klijentom():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['0.1', '0.2', '...', '0.8', '0.9', '1.0', '1.1']))

    graph.add_branch(mod_graph.Branch(
            branch_from = graph.find_node('1.0'),
            color = GRAY,
            row = 1,
            nodes = ['1.1\'', '1.2\'']))

    return graph

def graph_linearni_model():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', 'd', 'e', '1.0', 'f', 'g', 'h', 'i', '2.0', '...']))

    return graph

def graph_linearni_model_2():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', 'd', 'e', '1.0', 'f', 'g', 'h', 'i', '2.0', '...']))

    graph.add_branch(
        mod_graph.Branch(
            row = 1,
            nodes = ['x', 'y', '1.1'],
            color = GRAY,
            branch_from = graph.find_node('1.0')))

    graph.add_branch(
        mod_graph.Branch(
            row = 1,
            nodes = ['q', '2.1'],
            color = GRAY,
            branch_from = graph.find_node('2.0')))

    return graph

def graph_primjer_s_imenovanim_granama_i_spajanjima():
    graph = mod_graph.Graph(column = 5)

    graph.add_branch(mod_graph.Branch(
            label = 'master',	
            nodes = 'abcdefgh'))

    graph.add_branch(mod_graph.Branch(
            label = 'novi-feature',	
            row = 2,
            nodes = 'xyzqw',
            branch_from = graph.find_node('b')))

    graph.add_branch(mod_graph.Branch(
            label = 'ispravak-problema-x',	
            row = 1,
            nodes = '1234',
            branch_from = graph.find_node('g')))

    graph.add_arrow('d', 'z', color = GRAY)
    graph.add_arrow('q', 'g', color = GRAY)

    return graph

def graph_primjer_s_imenovanim_granama_i_spajanjima_suprotne_strelice():
    graph = mod_graph.Graph(column = 5)

    graph.add_branch(mod_graph.Branch(
            reverse_arrows = True,
            label = 'master',	
            nodes = 'abcdefgh'))

    graph.add_branch(mod_graph.Branch(
            reverse_arrows = True,
            label = 'novi-feature',	
            row = 2,
            nodes = 'xyzqw',
            branch_from = graph.find_node('b')))

    graph.add_branch(mod_graph.Branch(
            reverse_arrows = True,
            label = 'ispravak-problema-x',	
            row = 1,
            nodes = '1234',
            branch_from = graph.find_node('g')))

    graph.add_arrow('z', 'd', color = GRAY)
    graph.add_arrow('g', 'q', color = GRAY)

    return graph

def graph_primjer_s_granama_i_spajanjima():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = 'abcdefgh'))

    graph.add_branch(mod_graph.Branch(
            row = 2,
            nodes = 'xyzqw',
            branch_from = graph.find_node('b')))

    graph.add_branch(mod_graph.Branch(
            row = 1,
            nodes = '1234',
            branch_from = graph.find_node('g')))

    graph.add_arrow('d', 'z', color = GRAY)
    graph.add_arrow('q', 'g', color = GRAY)

    return graph

def graph_primjer_s_granama_i_spajanjima_1():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = 'abc'))

    return graph

def graph_primjer_s_granama_i_spajanjima_2():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = 'abc'))

    graph.add_branch(mod_graph.Branch(
            row = 1,
            nodes = 'xy',
            branch_from = graph.find_node('b')))

    return graph

def graph_primjer_s_granama_i_spajanjima_3():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = 'abcd'))

    graph.add_branch(mod_graph.Branch(
            row = 1,
            nodes = 'xy',
            branch_from = graph.find_node('b')))

    return graph

def graph_primjer_s_granama_i_spajanjima_4():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = 'abcd'))

    graph.add_branch(mod_graph.Branch(
            row = 1,
            nodes = 'xyz',
            branch_from = graph.find_node('b')))

    graph.add_arrow('d', 'z', color = GRAY)

    return graph

def graph_primjer_s_granama_i_spajanjima_5():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = 'abcdef'))

    graph.add_branch(mod_graph.Branch(
            row = 1,
            nodes = 'xyzq',
            branch_from = graph.find_node('b')))

    graph.add_arrow('d', 'z', color = GRAY)

    return graph

def graph_primjer_s_dugotrajnom_granom():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = 'abcdefghijklmnopq'))

    graph.add_branch(mod_graph.Branch(
            row = 1,
            nodes = '1234567890xyz',
            branch_from = graph.find_node('b')))

    graph.add_arrow('e', '4', color = GRAY)
    graph.add_arrow('h', '7', color = GRAY)
    graph.add_arrow('i', '8', color = GRAY)
    graph.add_arrow('l', 'x', color = GRAY)
    graph.add_arrow('n', 'z', color = GRAY)
    graph.add_arrow('z', 'p', color = RED)

    return graph

def graph_primjer_s_granama_i_spajanjima_6():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(
            row = 1,
            nodes = 'xyzq',
            branch_from = graph.find_node('b')))

    graph.add_arrow('d', 'z', color = GRAY)
    graph.add_arrow('q', 'g', color = GRAY)

    return graph

def graph_linearni_bez_zadnjeg_cvora_0():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c']))

    return graph

def graph_linearni_bez_zadnjeg_cvora_1():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', mod_graph.Node(label = ' ', color = WHITE)]))

    return graph

def graph_linearni_sa_zadnjim_cvorom():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', mod_graph.Node(label = 'd', color = BLUE)]))

    return graph

def graph_kreiranje_grane_1():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', mod_graph.Node(label = '', color = WHITE)]))

    return graph

def graph_kreiranje_grane_2():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = ['a', 'b', 'c', mod_graph.Node(label = '', color = WHITE)]))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperimentalna-grana',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = [mod_graph.Node(label = '', color = WHITE)]))

    return graph

def graph_kreiranje_grane_2_1():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = ['a', 'b', 'c', mod_graph.Node(label = '', color = WHITE)]))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperimentalna-grana',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = 'd'))

    return graph

def graph_kreiranje_grane_3():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = ['a', 'b', 'c', mod_graph.Node(label = '', color = WHITE)]))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperimentalna-grana',
            color = BLUE,
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = 'defg'))

    return graph

def graph_kreiranje_grane_4():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            color = BLUE,
            nodes = 'abcxyz'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperimentalna-grana',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = 'defg'))

    return graph

def graph_git_merge_i_brisanje_grana_1():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcxyzq'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperiment',
            branch_from = graph.find_node('b'),
            row = 1,
            nodes = 'defg'))

    return graph

def graph_git_merge_i_brisanje_grana_2():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcxyzq'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperiment',
            branch_from = graph.find_node('b'),
            row = 1,
            nodes = 'defg'))

    graph.add_arrow('g', 'q', color = GRAY)

    return graph

def graph_git_merge_i_brisanje_grana_3():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcxyzq'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperiment',
            branch_from = graph.find_node('b'),
            row = 1,
            nodes = 'defg'))

    graph.add_arrow('f', 'z', color = GRAY)

    return graph

def graph_git_merge_i_brisanje_grana_4():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcxyzq'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperiment',
            branch_from = graph.find_node('b'),
            row = 1,
            nodes = 'defg'))

    graph.add_arrow('g', 'q', color = RED)

    return graph

def graph_git_merge_i_brisanje_grana_5():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcxyzq'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperiment',
            branch_from = graph.find_node('b'),
            row = 1,
            nodes = 'defg'))

    return graph

def graph_git_merge_01():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            color = BLUE,
            nodes = 'abc'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperimentalna-grana',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = [mod_graph.Node(' ', color=WHITE)]))

    return graph

def graph_git_merge_02():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            color = BLUE,
            nodes = 'abcxyzq'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperimentalna-grana',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = [mod_graph.Node(' ', color=WHITE)]))

    return graph

def graph_git_merge_1():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            color = BLUE,
            nodes = 'abcxyzq'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperimentalna-grana',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = 'defg'))

    return graph

def graph_git_merge_2():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            color = BLUE,
            nodes = 'abcxyzqh'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperimentalna-grana',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = 'defg'))

    graph.add_arrow('g', 'h', color = GRAY)

    return graph

def graph_git_merge_3():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            color = BLUE,
            nodes = 'abcxyzq 123'))

    graph.add_branch(mod_graph.Branch(
            label = 'eksperimentalna-grana',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = 'defg567'))

    graph.add_arrow('g', ' ', color = GRAY)
    graph.add_arrow('7', '3', color = GRAY)
    graph.add_arrow('1', '7', color = GRAY)

    return graph

def graph_ab_simic_1():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'ab'))

    graph.add_branch(mod_graph.Branch(
            label = 'varijanta',
            branch_from = graph.find_node('a'),
            row = 1,
            nodes = 'c'))

    return graph

def graph_ab_simic_2():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abd'))

    graph.add_branch(mod_graph.Branch(
            label = 'varijanta',
            branch_from = graph.find_node('a'),
            row = 1,
            nodes = 'c'))

    graph.add_arrow('c', 'd', color = GRAY)

    return graph

def graph_bez_fast_forward():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcdef'))

    graph.add_branch(mod_graph.Branch(
            label = 'varijanta',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = 'xyz'))

    return graph

def graph_bez_fast_forward_rebase():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcdef'))

    graph.add_branch(mod_graph.Branch(
            label = 'varijanta',
            branch_from = graph.find_node('f'),
            row = 1,
            nodes = ['x\'', 'y\'', 'z\'']))

    return graph

def graph_bez_fast_forward_rebase_2():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'x\'', 'y\'', 'z\'']))

    return graph

def graph_fast_forward():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abc'))

    graph.add_branch(mod_graph.Branch(
            label = 'varijanta',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = 'xyz'))

    return graph

def graph_fast_forward_2():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abc---d'))

    graph.add_branch(mod_graph.Branch(
            label = 'varijanta',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = 'xyz'))

    graph.add_arrow('z', 'd', color = GRAY)

    return graph

def graph_fast_forward_3():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcxyz'))

    graph.add_branch(mod_graph.Branch(
            label = 'varijanta',
            branch_from = graph.find_node('c'),
            row = 1,
            nodes = 'xyz'))

    return graph

def graph_fast_forward_4():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcdef'))

    graph.add_branch(mod_graph.Branch(
            label = 'varijanta',
            branch_from = graph.find_node('c'),
            color = GRAY,
            row = 1,
            nodes = 'xyz'))

    graph.add_branch(mod_graph.Branch(
            label = 'varijanta',
            branch_from = graph.find_node('f'),
            color = BLUE,
            row = 1,
            nodes = ['x\'', 'y\'', 'z\'']))

    return graph

def graph_linearni_model_za_reset():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', 'd', 'e', mod_graph.Node(label = 'f', color = RED), mod_graph.Node(label = 'g', color = RED), mod_graph.Node(label = 'h', color = RED), mod_graph.Node(label = 'i', color = RED), mod_graph.Node(label = '...', color = RED)]))

    return graph

def graph_linearni_model_za_reset():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', 'd', 'e', mod_graph.Node(label = 'f', color = RED), mod_graph.Node(label = 'g', color = RED), mod_graph.Node(label = 'h', color = RED), mod_graph.Node(label = 'i', color = RED),]))

    return graph

def graph_linearni_model_za_reset_2():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = 'abcde'))

    return graph

def graph_linearni_model_za_reset_HEAD_1():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            reverse_arrows = True,
            nodes = ['a', 'b', 'c', 'd', 'e', mod_graph.Node(label = 'f', color = RED), mod_graph.Node(label = 'g', color = RED), mod_graph.Node(label = 'h', color = RED), mod_graph.Node(label = 'i(HEAD)', color = RED),]))

    return graph

def graph_linearni_model_za_reset_HEAD_2():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            reverse_arrows = True,
            nodes = ['a', 'b', 'c', 'd', 'e(HEAD)', '-', '-', mod_graph.Node(label = 'f', color = RED), mod_graph.Node(label = 'g', color = RED), mod_graph.Node(label = 'h', color = RED), mod_graph.Node(label = 'i', color = RED),]))

    return graph

def graph_linearni_model_za_revert_1():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', 'd', 'e', mod_graph.Node(label = 'f', color = RED)]))

    return graph

def graph_linearni_model_za_revert_1_revertano():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', 'd', 'e', mod_graph.Node(label = 'f', color = RED), 'g']))

    return graph

def graph_linearni_model_za_revert_2():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', 'd', 'e', mod_graph.Node(label = 'f', color = RED), 'g', 'h', 'i']))

    return graph

def graph_linearni_model_za_revert_2_revertano():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = ['a', 'b', 'c', 'd', 'e', mod_graph.Node(label = 'f', color = RED), 'g', 'h', 'i', 'j']))

    return graph

def graph_origin_master():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcde'))

    brackets_column = 9 

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_origin_master_2():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdefg'))

    brackets_column = 11 

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_origin_master_2_2():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcdexy'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdefg'))

    brackets_column = 11 

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_origin_master_2_3():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcdexy'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdefg'))

    brackets_column = 11 

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_origin_master_2_3():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcdexy'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdefg'))

    brackets_column = 11 

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_origin_master_2_4():
    graph = mod_graph.Graph(column = 4)

    master_branch = mod_graph.Branch(
            label = 'master',
            nodes = 'abcdexyz')
    graph.add_branch(master_branch)

    origin_master_branch = mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcdefg')
    graph.add_branch(origin_master_branch)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdefg'))

    brackets_column = 12 

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    graph.add_arrow(
            origin_master_branch.find_node('g'),
            master_branch.find_node('z'),
            color = GRAY)

    return graph

def graph_origin_master_3():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdefg'))

    brackets_column = 11 

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_origin_master_4():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdefg'))

    brackets_column = 11 

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_push_1():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcde'))

    brackets_column = 9 

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_push_2():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcde'))

    brackets_column = 11

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_push_2_1():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdexy'))

    brackets_column = 11

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_push_2_2():
    graph = mod_graph.Graph(column = 4)

    master_branch = mod_graph.Branch(
            label = 'master',
            nodes = 'abcdefg')
    graph.add_branch(master_branch)

    origin_master_branch = mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcdexy')
    graph.add_branch(origin_master_branch)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdexy'))

    brackets_column = 11

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_push_2_2_1():
    graph = mod_graph.Graph(column = 4)

    master_branch = mod_graph.Branch(
            label = 'master',
            nodes = 'abcdefg')
    graph.add_branch(master_branch)

    origin_master_branch = mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcdexy')
    graph.add_branch(origin_master_branch)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdefg'))

    brackets_column = 11

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_push_2_3():
    graph = mod_graph.Graph(column = 4)

    master_branch = mod_graph.Branch(
            label = 'master',
            nodes = 'abcdefgh')
    graph.add_branch(master_branch)

    origin_master_branch = mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcdexy')
    graph.add_branch(origin_master_branch)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdexy'))

    brackets_column = 12

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    graph.add_arrow(
            origin_master_branch.find_node('y'),
            master_branch.find_node('h'),
            color = GRAY)

    return graph

def graph_push_2_4():
    graph = mod_graph.Graph(column = 4)

    master_branch = mod_graph.Branch(
            label = 'master',
            nodes = 'abcdefgh')
    graph.add_branch(master_branch)

    origin_master_branch = mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcdexy')
    graph.add_branch(origin_master_branch)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdexyh'))
    graph.add_branch(mod_graph.Branch(
            label = '',
            row = 4,
            branch_from = graph.get_branch(2).get_node(4),
            nodes = 'fg'))
    graph.add_arrow(graph.get_branch(3).get_node(1),
                    graph.get_branch(2).get_node(7),
                    color=GRAY)

    brackets_column = 12

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 2,
            label = 'udaljeni repozitorij')

    graph.add_arrow(
            origin_master_branch.find_node('y'),
            master_branch.find_node('h'),
            color = GRAY)

    return graph

def graph_push_3():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(
            label = 'master',
            row = 3,
            nodes = 'abcdefg'))

    brackets_column = 11

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 2,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 3,
            rows = 1,
            label = 'udaljeni repozitorij')

    return graph

def graph_digresija_o_grafovima_1():
    graph = mod_graph.Graph(column = 3)

    graph.add_branch(mod_graph.Branch(
            label = 'grana-1',
            nodes = 'abcdefghij'))

    graph.add_branch(mod_graph.Branch(
            label = 'grana-2',
            row = 1,
            nodes = 'abcdeyzq'))

    return graph

def graph_digresija_o_grafovima_2():
    graph = mod_graph.Graph(column = 3)

    graph.add_branch(mod_graph.Branch(
            label = 'grana-1',
            nodes = 'abcdefghij'))

    graph.add_branch(mod_graph.Branch(
            label = 'grana-2',
            row = 1,
            branch_from = graph.get_branch(0).get_node(4),
            nodes = 'yzq'))

    return graph

def graph_digresija_o_grafovima_3():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(label = 'master', nodes = 'abcdexy'))

    graph.add_branch(mod_graph.Branch(label = 'origin/master', row = 1, nodes = 'abcde'))

    graph.add_branch(mod_graph.Branch(label = 'master', row = 3, nodes = 'abcdefg'))

    brackets_column = 11 

    graph.add_square_bracket(column = brackets_column, row = 0, rows = 2, label = 'lokalni repozitorij')

    graph.add_square_bracket(column = brackets_column, row = 3, rows = 1, label = 'udaljeni repozitorij')

    return graph

def graph_digresija_o_grafovima_4():
    graph = mod_graph.Graph(column = 4)

    graph.add_branch(mod_graph.Branch(label = 'master', nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(label = 'master', row = 1, nodes = 'xy',
                                        branch_from = graph.get_branch(0).get_node(4)))

    brackets_column = 11 

    graph.add_square_bracket(column = brackets_column, row = 0, rows = 1,
                              label = 'udaljeni repozitorij')

    graph.add_square_bracket(column = brackets_column, row = 1, rows = 1,
                              label = 'lokalni repozitorij')

    return graph

def graph_origin_master_s_granama():
    graph = mod_graph.Graph(column = 4)

    master_branch = mod_graph.Branch(
            label = 'master',
            nodes = 'abcde')
    graph.add_branch(master_branch)

    origin_master_branch = mod_graph.Branch(
            label = 'origin/master',
            row = 1,
            nodes = 'abcde')
    graph.add_branch(origin_master_branch)

    graph.add_branch(mod_graph.Branch(
            label = 'origin/grana',
            row = 2,
            branch_from = origin_master_branch.get_node(2),
            nodes = 'xyz'))

    remote_master_branch = mod_graph.Branch(
            label = 'master',
            row = 4,
            nodes = 'abcde')
    graph.add_branch(remote_master_branch)

    graph.add_branch(mod_graph.Branch(
            label = 'grana',
            row = 5,
            branch_from = remote_master_branch.get_node(2),
            nodes = 'xyz'))

    brackets_column = 10

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 3,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 4,
            rows = 2,
            label = 'udaljeni repozitorij')

    return graph

def graph_origin_master_s_granama_2():
    graph = mod_graph.Graph(column = 4)

    master_branch = mod_graph.Branch(
            label = 'master',
            nodes = 'abcde')
    graph.add_branch(master_branch)

    graph.add_branch(mod_graph.Branch(
            label = 'grana',
            row = 1,
            branch_from = master_branch.get_node(2),
            nodes = 'xyz'))

    origin_master_branch = mod_graph.Branch(
            label = 'origin/master',
            row = 2,
            nodes = 'abcde')
    graph.add_branch(origin_master_branch)

    graph.add_branch(mod_graph.Branch(
            label = 'origin/grana',
            row = 3,
            branch_from = origin_master_branch.get_node(2),
            nodes = 'xyz'))

    remote_master_branch = mod_graph.Branch(
            label = 'master',
            row = 5,
            nodes = 'abcde')
    graph.add_branch(remote_master_branch)

    graph.add_branch(mod_graph.Branch(
            label = 'grana',
            row = 6,
            branch_from = remote_master_branch.get_node(2),
            nodes = 'xyz'))

    brackets_column = 10

    graph.add_square_bracket(
            column = brackets_column,
            row = 0,
            rows = 4,
            label = 'lokalni repozitorij')

    graph.add_square_bracket(
            column = brackets_column,
            row = 5,
            rows = 2,
            label = 'udaljeni repozitorij')

    return graph

def graph_remote_s_granama():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(label = 'master', nodes = 'abcdefg'))
    graph.add_branch(mod_graph.Branch(label = 'karlin-repo/master', row = 1, nodes = 'abcdefg'))
    graph.add_branch(mod_graph.Branch(label = 'bojanov-repo/master', row = 2, nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(label = 'master', row = 4, nodes = 'abcdefg'))

    graph.add_branch(mod_graph.Branch(label = 'master', row = 6, nodes = 'abcdefg'))

    brackets_column = 13 

    graph.add_square_bracket(column = brackets_column, row = 0, rows = 3, label = 'lokalni repozitorij')
    graph.add_square_bracket(column = brackets_column, row = 4, rows = 1, label = 'Karlin repozitorij')
    graph.add_square_bracket(column = brackets_column, row = 6, rows = 1, label = 'Bojanov repozitorij')

    return graph

def graph_remote_s_granama_2():
    graph = mod_graph.Graph(column = 6)

    graph.add_branch(mod_graph.Branch(label = 'master', nodes = 'abcdefg'))
    karlin_master_lokalni = mod_graph.Branch(label = 'karlin-repo/master', row = 1, nodes = 'abcdefg')
    graph.add_branch(karlin_master_lokalni)
    graph.add_branch(mod_graph.Branch(branch_from = karlin_master_lokalni.get_node(3), row = 2, nodes = 'xyz', label = 'karlin-repo/varijanta-1'))

    bojanov_master_lokalni = mod_graph.Branch(label = 'bojanov-repo/master', row = 3, nodes = 'abcdefg')
    graph.add_branch(bojanov_master_lokalni)
    graph.add_branch(mod_graph.Branch(branch_from = bojanov_master_lokalni.get_node(2), row = 4, nodes = 'qwe', label = 'bojanov-repo/test'))

    karlin_master = mod_graph.Branch(label = 'master', row = 6, nodes = 'abcdefg')
    graph.add_branch(karlin_master)
    graph.add_branch(mod_graph.Branch(branch_from = karlin_master.get_node(3), row = 7, nodes = 'xyz', label = 'varijanta-1'))

    bojanov_master = mod_graph.Branch(label = 'master', row = 9, nodes = 'abcdefg')
    graph.add_branch(bojanov_master)
    graph.add_branch(mod_graph.Branch(branch_from = bojanov_master.get_node(2), row = 10, nodes = 'qwe', label = 'test'))

    brackets_column = 13 

    graph.add_square_bracket(column = brackets_column, row = 0, rows = 5, label = 'lokalni repozitorij')
    graph.add_square_bracket(column = brackets_column, row = 6, rows = 2, label = 'Karlin repozitorij')
    graph.add_square_bracket(column = brackets_column, row = 9, rows = 2, label = 'Bojanov repozitorij')

    return graph

def graph_cirkus():
    graph = mod_graph.Graph(node_distance=200)

    for i in range(16):
        nodes = ''
        for j in range(mod_random.randint(5,15)):
            nodes += ' '
        if i == 0:
            graph.add_branch(mod_graph.Branch(nodes=nodes, row=i))
        else:
            random_branch = graph.get_branch(mod_random.randint(max(0, i - 2), i - 1))
            graph.add_branch(mod_graph.Branch(branch_from=random_branch.get_node(mod_random.randint(0,1)),
                                              nodes=nodes, row=i))
            graph.add_arrow(graph.get_branch(i).get_node(mod_random.randint(1, 2)),
                            graph.get_branch(i - 1).get_node(mod_random.randint(2, 3)),
                            color=GRAY)

    return graph

def graph_amend():
    graph = mod_graph.Graph(column=3)

    graph.add_branch(mod_graph.Branch(label='master', row=0, nodes=('a','b','c','d','e','f\'')))
    graph.add_branch(mod_graph.Branch(label='master', row=2, nodes='abcdef'))

    graph.add_square_bracket(column = 9, row = 2, rows = 1, label = 'Originalno stanje')
    graph.add_square_bracket(column = 9, row = 0, rows = 1, label = 'Nakon commit --amend')

    return graph

def graph_bisect_1():
    graph = mod_graph.Graph()

    graph.add_branch(mod_graph.Branch(
            nodes = [
                    'a',
                    'b',
                    mod_graph.Node(label='c', color=BLUE),
                    'd',
                    'e',
                    '1.0',
                    'f',
                    'g',
                    'h',
                    'i',
                    '2.0',
                    'j',
                    mod_graph.Node(label='k', color=RED)]))

    return graph

def graph_izrazi_s_referencama():
    graph = mod_graph.Graph(column=3)

    graph.add_branch(mod_graph.Branch(
            nodes = 'abcdefg', label='master'))

    graph.add_branch(mod_graph.Branch(
            row=1,
            nodes='xyzq',
            label='test',
            branch_from = graph.find_node('b')))

    graph.add_arrow('d', 'z', color = GRAY)
    graph.add_arrow('q', 'g', color = GRAY)

    return graph

def graph_izrazi_s_referencama_2():
    graph = mod_graph.Graph(column=3)

    graph.add_branch(mod_graph.Branch(
            nodes = 'abcdefgh', label='master'))

    graph.add_branch(mod_graph.Branch(
            row=1,
            nodes='xyzq',
            label='test',
            branch_from = graph.find_node('b')))

    graph.add_arrow('d', 'z', color = GRAY)
    graph.add_arrow('q', 'g', color = GRAY)

    return graph

for v in vars().keys():
    # create graphs/ director if not exists:
    try:
        mod_os.mkdir('graphs')
    except:
        pass

    if v.startswith('graph_'):
        method = vars()[v]
        file_name = 'graphs/' + v.replace('graph_', '') + '.tex'

        graph = method()

        with file(file_name, 'w') as f:
            f.write("""\\begin{tabular}{l}
    \\begin{minipage}[b]{150mm}%
        \\vspace*{3mm}%
        \\noindent""")
            f.write(graph.get_latex_string())
            f.write("""\\end{minipage}%
\\end{tabular}
""")
            print file_name, ' OK'
		

