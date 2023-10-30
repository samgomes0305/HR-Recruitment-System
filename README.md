# HR-Recruitment-System

Here is a sample Python readme for this Recruitment Management System. It provides a platform for creating and managing an applicant pool, which consists of already filtered candidates with respect to existing parameters.

## How it works

The code consists of two main classes:

1. `Candidate`: This refers to a job applicant, as described in this class. The attributes of the candidate’s name, interview, theory, practical, and general skills score are contained in it. The procedure also contains a mechanism for determining whether the candidate attains the set threshold.

2. `CandidateSet`: This is a container class that manages a set of candidates. You are able to add the candidates into the set and filter them out by their lowest scores in distinct assessment fields.

## Usage

1. For every candidate you would like to include, create a `Candidate` object.
2. The `adicionar_candidato` method can be used to add candidates into the `CandidateSet`.
3. State down the lowest marks for the interview, theoretical exam, practical examination, and interpersonal skills.
4. Retrieve candidates that meet specific criteria using “buscar_candidatos_atendendo_critério”.
5. This code will give you a list of the matching/ non-matching candidates.

You are free to modify as required in order to conform to your unique recruitment practices.

## Getting Started

For this code to work, you must have Python installed in your system. Download the code and run it through a Python interpreter.

```bash
python hr_recruitment_system.py

Author
Samuel Galvão Gomes
