import random

# Lista de perguntas (exemplo com 5, depois podemos expandir)
perguntas = [
    {
        "pergunta": "O que é um algoritmo?",
        "opcoes": ["Um tipo de linguagem", "Uma sequência de passos", "Um código-fonte", "Um hardware"],
        "resposta": "Uma sequência de passos",
        "dica": "Pense na lógica antes da linguagem."
    },
    {
        "pergunta": "Qual destas é uma estrutura de repetição?",
        "opcoes": ["if", "while", "else", "print"],
        "resposta": "while",
        "dica": "Ela repete até uma condição ser falsa."
    },
    {
        "pergunta": "Qual é o operador de igualdade em Python?",
        "opcoes": ["=", "==", "!=", "==="],
        "resposta": "==",
        "dica": "É uma comparação, não uma atribuição."
    },
    {
        "pergunta": "Qual função exibe algo na tela em Python?",
        "opcoes": ["echo", "printf", "show", "print"],
        "resposta": "print",
        "dica": "É a mais usada para mostrar resultados."
    },
    {
        "pergunta": "Como declaramos uma função em Python?",
        "opcoes": ["function", "def", "func", "declare"],
        "resposta": "def",
        "dica": "Vem antes do nome da função."
    }

    {
        "pergunta": "O que é um algoritmo?",
        "opcoes": [
            "Um tipo de linguagem",
            "Uma sequência de passos",
            "Um código-fonte",
            "Um hardware"
        ],
        "resposta": "Uma sequência de passos",
        "dica": "Pense na lógica antes da linguagem."
    },
    {
        "pergunta": "Qual destas é uma estrutura de repetição?",
        "opcoes": [
            "if",
            "while",
            "else",
            "print"
        ],
        "resposta": "while",
        "dica": "Ela repete até uma condição ser falsa."
    },
    {
        "pergunta": "Qual é o operador de igualdade em Python?",
        "opcoes": [
            "=",
            "==",
            "!=",
            "==="
        ],
        "resposta": "==",
        "dica": "É uma comparação, não uma atribuição."
    },
    {
        "pergunta": "Qual função exibe algo na tela em Python?",
        "opcoes": [
            "echo",
            "printf",
            "show",
            "print"
        ],
        "resposta": "print",
        "dica": "É a mais usada para mostrar resultados."
    },
    {
        "pergunta": "Como declaramos uma função em Python?",
        "opcoes": [
            "function",
            "def",
            "func",
            "declare"
        ],
        "resposta": "def",
        "dica": "Vem antes do nome da função."
    },
    {
        "pergunta": "Pergunta de exemplo número 6?",
        "opcoes": [
            "Opção A6",
            "Opção B6",
            "Opção C6",
            "Opção D6"
        ],
        "resposta": "Opção B6",
        "dica": "Dica para a pergunta número 6."
    },
    {
        "pergunta": "Pergunta de exemplo número 7?",
        "opcoes": [
            "Opção A7",
            "Opção B7",
            "Opção C7",
            "Opção D7"
        ],
        "resposta": "Opção B7",
        "dica": "Dica para a pergunta número 7."
    },
    {
        "pergunta": "Pergunta de exemplo número 8?",
        "opcoes": [
            "Opção A8",
            "Opção B8",
            "Opção C8",
            "Opção D8"
        ],
        "resposta": "Opção B8",
        "dica": "Dica para a pergunta número 8."
    },
    {
        "pergunta": "Pergunta de exemplo número 9?",
        "opcoes": [
            "Opção A9",
            "Opção B9",
            "Opção C9",
            "Opção D9"
        ],
        "resposta": "Opção B9",
        "dica": "Dica para a pergunta número 9."
    },
    {
        "pergunta": "Pergunta de exemplo número 10?",
        "opcoes": [
            "Opção A10",
            "Opção B10",
            "Opção C10",
            "Opção D10"
        ],
        "resposta": "Opção B10",
        "dica": "Dica para a pergunta número 10."
    },
    {
        "pergunta": "Pergunta de exemplo número 11?",
        "opcoes": [
            "Opção A11",
            "Opção B11",
            "Opção C11",
            "Opção D11"
        ],
        "resposta": "Opção B11",
        "dica": "Dica para a pergunta número 11."
    },
    {
        "pergunta": "Pergunta de exemplo número 12?",
        "opcoes": [
            "Opção A12",
            "Opção B12",
            "Opção C12",
            "Opção D12"
        ],
        "resposta": "Opção B12",
        "dica": "Dica para a pergunta número 12."
    },
    {
        "pergunta": "Pergunta de exemplo número 13?",
        "opcoes": [
            "Opção A13",
            "Opção B13",
            "Opção C13",
            "Opção D13"
        ],
        "resposta": "Opção B13",
        "dica": "Dica para a pergunta número 13."
    },
    {
        "pergunta": "Pergunta de exemplo número 14?",
        "opcoes": [
            "Opção A14",
            "Opção B14",
            "Opção C14",
            "Opção D14"
        ],
        "resposta": "Opção B14",
        "dica": "Dica para a pergunta número 14."
    },
    {
        "pergunta": "Pergunta de exemplo número 15?",
        "opcoes": [
            "Opção A15",
            "Opção B15",
            "Opção C15",
            "Opção D15"
        ],
        "resposta": "Opção B15",
        "dica": "Dica para a pergunta número 15."
    },
    {
        "pergunta": "Pergunta de exemplo número 16?",
        "opcoes": [
            "Opção A16",
            "Opção B16",
            "Opção C16",
            "Opção D16"
        ],
        "resposta": "Opção B16",
        "dica": "Dica para a pergunta número 16."
    },
    {
        "pergunta": "Pergunta de exemplo número 17?",
        "opcoes": [
            "Opção A17",
            "Opção B17",
            "Opção C17",
            "Opção D17"
        ],
        "resposta": "Opção B17",
        "dica": "Dica para a pergunta número 17."
    },
    {
        "pergunta": "Pergunta de exemplo número 18?",
        "opcoes": [
            "Opção A18",
            "Opção B18",
            "Opção C18",
            "Opção D18"
        ],
        "resposta": "Opção B18",
        "dica": "Dica para a pergunta número 18."
    },
    {
        "pergunta": "Pergunta de exemplo número 19?",
        "opcoes": [
            "Opção A19",
            "Opção B19",
            "Opção C19",
            "Opção D19"
        ],
        "resposta": "Opção B19",
        "dica": "Dica para a pergunta número 19."
    },
    {
        "pergunta": "Pergunta de exemplo número 20?",
        "opcoes": [
            "Opção A20",
            "Opção B20",
            "Opção C20",
            "Opção D20"
        ],
        "resposta": "Opção B20",
        "dica": "Dica para a pergunta número 20."
    },
    {
        "pergunta": "Pergunta de exemplo número 21?",
        "opcoes": [
            "Opção A21",
            "Opção B21",
            "Opção C21",
            "Opção D21"
        ],
        "resposta": "Opção B21",
        "dica": "Dica para a pergunta número 21."
    },
    {
        "pergunta": "Pergunta de exemplo número 22?",
        "opcoes": [
            "Opção A22",
            "Opção B22",
            "Opção C22",
            "Opção D22"
        ],
        "resposta": "Opção B22",
        "dica": "Dica para a pergunta número 22."
    },
    {
        "pergunta": "Pergunta de exemplo número 23?",
        "opcoes": [
            "Opção A23",
            "Opção B23",
            "Opção C23",
            "Opção D23"
        ],
        "resposta": "Opção B23",
        "dica": "Dica para a pergunta número 23."
    },
    {
        "pergunta": "Pergunta de exemplo número 24?",
        "opcoes": [
            "Opção A24",
            "Opção B24",
            "Opção C24",
            "Opção D24"
        ],
        "resposta": "Opção B24",
        "dica": "Dica para a pergunta número 24."
    },
    {
        "pergunta": "Pergunta de exemplo número 25?",
        "opcoes": [
            "Opção A25",
            "Opção B25",
            "Opção C25",
            "Opção D25"
        ],
        "resposta": "Opção B25",
        "dica": "Dica para a pergunta número 25."
    },
    {
        "pergunta": "Pergunta de exemplo número 26?",
        "opcoes": [
            "Opção A26",
            "Opção B26",
            "Opção C26",
            "Opção D26"
        ],
        "resposta": "Opção B26",
        "dica": "Dica para a pergunta número 26."
    },
    {
        "pergunta": "Pergunta de exemplo número 27?",
        "opcoes": [
            "Opção A27",
            "Opção B27",
            "Opção C27",
            "Opção D27"
        ],
        "resposta": "Opção B27",
        "dica": "Dica para a pergunta número 27."
    },
    {
        "pergunta": "Pergunta de exemplo número 28?",
        "opcoes": [
            "Opção A28",
            "Opção B28",
            "Opção C28",
            "Opção D28"
        ],
        "resposta": "Opção B28",
        "dica": "Dica para a pergunta número 28."
    },
    {
        "pergunta": "Pergunta de exemplo número 29?",
        "opcoes": [
            "Opção A29",
            "Opção B29",
            "Opção C29",
            "Opção D29"
        ],
        "resposta": "Opção B29",
        "dica": "Dica para a pergunta número 29."
    },
    {
        "pergunta": "Pergunta de exemplo número 30?",
        "opcoes": [
            "Opção A30",
            "Opção B30",
            "Opção C30",
            "Opção D30"
        ],
        "resposta": "Opção B30",
        "dica": "Dica para a pergunta número 30."
    },
    {
        "pergunta": "Pergunta de exemplo número 31?",
        "opcoes": [
            "Opção A31",
            "Opção B31",
            "Opção C31",
            "Opção D31"
        ],
        "resposta": "Opção B31",
        "dica": "Dica para a pergunta número 31."
    },
    {
        "pergunta": "Pergunta de exemplo número 32?",
        "opcoes": [
            "Opção A32",
            "Opção B32",
            "Opção C32",
            "Opção D32"
        ],
        "resposta": "Opção B32",
        "dica": "Dica para a pergunta número 32."
    },
    {
        "pergunta": "Pergunta de exemplo número 33?",
        "opcoes": [
            "Opção A33",
            "Opção B33",
            "Opção C33",
            "Opção D33"
        ],
        "resposta": "Opção B33",
        "dica": "Dica para a pergunta número 33."
    },
    {
        "pergunta": "Pergunta de exemplo número 34?",
        "opcoes": [
            "Opção A34",
            "Opção B34",
            "Opção C34",
            "Opção D34"
        ],
        "resposta": "Opção B34",
        "dica": "Dica para a pergunta número 34."
    },
    {
        "pergunta": "Pergunta de exemplo número 35?",
        "opcoes": [
            "Opção A35",
            "Opção B35",
            "Opção C35",
            "Opção D35"
        ],
        "resposta": "Opção B35",
        "dica": "Dica para a pergunta número 35."
    },
    {
        "pergunta": "Pergunta de exemplo número 36?",
        "opcoes": [
            "Opção A36",
            "Opção B36",
            "Opção C36",
            "Opção D36"
        ],
        "resposta": "Opção B36",
        "dica": "Dica para a pergunta número 36."
    },
    {
        "pergunta": "Pergunta de exemplo número 37?",
        "opcoes": [
            "Opção A37",
            "Opção B37",
            "Opção C37",
            "Opção D37"
        ],
        "resposta": "Opção B37",
        "dica": "Dica para a pergunta número 37."
    },
    {
        "pergunta": "Pergunta de exemplo número 38?",
        "opcoes": [
            "Opção A38",
            "Opção B38",
            "Opção C38",
            "Opção D38"
        ],
        "resposta": "Opção B38",
        "dica": "Dica para a pergunta número 38."
    },
    {
        "pergunta": "Pergunta de exemplo número 39?",
        "opcoes": [
            "Opção A39",
            "Opção B39",
            "Opção C39",
            "Opção D39"
        ],
        "resposta": "Opção B39",
        "dica": "Dica para a pergunta número 39."
    },
    {
        "pergunta": "Pergunta de exemplo número 40?",
        "opcoes": [
            "Opção A40",
            "Opção B40",
            "Opção C40",
            "Opção D40"
        ],
        "resposta": "Opção B40",
        "dica": "Dica para a pergunta número 40."
    },
    {
        "pergunta": "Pergunta de exemplo número 41?",
        "opcoes": [
            "Opção A41",
            "Opção B41",
            "Opção C41",
            "Opção D41"
        ],
        "resposta": "Opção B41",
        "dica": "Dica para a pergunta número 41."
    },
    {
        "pergunta": "Pergunta de exemplo número 42?",
        "opcoes": [
            "Opção A42",
            "Opção B42",
            "Opção C42",
            "Opção D42"
        ],
        "resposta": "Opção B42",
        "dica": "Dica para a pergunta número 42."
    },
    {
        "pergunta": "Pergunta de exemplo número 43?",
        "opcoes": [
            "Opção A43",
            "Opção B43",
            "Opção C43",
            "Opção D43"
        ],
        "resposta": "Opção B43",
        "dica": "Dica para a pergunta número 43."
    },
    {
        "pergunta": "Pergunta de exemplo número 44?",
        "opcoes": [
            "Opção A44",
            "Opção B44",
            "Opção C44",
            "Opção D44"
        ],
        "resposta": "Opção B44",
        "dica": "Dica para a pergunta número 44."
    },
    {
        "pergunta": "Pergunta de exemplo número 45?",
        "opcoes": [
            "Opção A45",
            "Opção B45",
            "Opção C45",
            "Opção D45"
        ],
        "resposta": "Opção B45",
        "dica": "Dica para a pergunta número 45."
    },
    {
        "pergunta": "Pergunta de exemplo número 46?",
        "opcoes": [
            "Opção A46",
            "Opção B46",
            "Opção C46",
            "Opção D46"
        ],
        "resposta": "Opção B46",
        "dica": "Dica para a pergunta número 46."
    },
    {
        "pergunta": "Pergunta de exemplo número 47?",
        "opcoes": [
            "Opção A47",
            "Opção B47",
            "Opção C47",
            "Opção D47"
        ],
        "resposta": "Opção B47",
        "dica": "Dica para a pergunta número 47."
    },
    {
        "pergunta": "Pergunta de exemplo número 48?",
        "opcoes": [
            "Opção A48",
            "Opção B48",
            "Opção C48",
            "Opção D48"
        ],
        "resposta": "Opção B48",
        "dica": "Dica para a pergunta número 48."
    },
    {
        "pergunta": "Pergunta de exemplo número 49?",
        "opcoes": [
            "Opção A49",
            "Opção B49",
            "Opção C49",
            "Opção D49"
        ],
        "resposta": "Opção B49",
        "dica": "Dica para a pergunta número 49."
    },
    {
        "pergunta": "Pergunta de exemplo número 50?",
        "opcoes": [
            "Opção A50",
            "Opção B50",
            "Opção C50",
            "Opção D50"
        ],
        "resposta": "Opção B50",
        "dica": "Dica para a pergunta número 50."
    },
    {
        "pergunta": "Pergunta de exemplo número 51?",
        "opcoes": [
            "Opção A51",
            "Opção B51",
            "Opção C51",
            "Opção D51"
        ],
        "resposta": "Opção B51",
        "dica": "Dica para a pergunta número 51."
    },
    {
        "pergunta": "Pergunta de exemplo número 52?",
        "opcoes": [
            "Opção A52",
            "Opção B52",
            "Opção C52",
            "Opção D52"
        ],
        "resposta": "Opção B52",
        "dica": "Dica para a pergunta número 52."
    },
    {
        "pergunta": "Pergunta de exemplo número 53?",
        "opcoes": [
            "Opção A53",
            "Opção B53",
            "Opção C53",
            "Opção D53"
        ],
        "resposta": "Opção B53",
        "dica": "Dica para a pergunta número 53."
    },
    {
        "pergunta": "Pergunta de exemplo número 54?",
        "opcoes": [
            "Opção A54",
            "Opção B54",
            "Opção C54",
            "Opção D54"
        ],
        "resposta": "Opção B54",
        "dica": "Dica para a pergunta número 54."
    },
    {
        "pergunta": "Pergunta de exemplo número 55?",
        "opcoes": [
            "Opção A55",
            "Opção B55",
            "Opção C55",
            "Opção D55"
        ],
        "resposta": "Opção B55",
        "dica": "Dica para a pergunta número 55."
    },
    {
        "pergunta": "Pergunta de exemplo número 56?",
        "opcoes": [
            "Opção A56",
            "Opção B56",
            "Opção C56",
            "Opção D56"
        ],
        "resposta": "Opção B56",
        "dica": "Dica para a pergunta número 56."
    },
    {
        "pergunta": "Pergunta de exemplo número 57?",
        "opcoes": [
            "Opção A57",
            "Opção B57",
            "Opção C57",
            "Opção D57"
        ],
        "resposta": "Opção B57",
        "dica": "Dica para a pergunta número 57."
    },
    {
        "pergunta": "Pergunta de exemplo número 58?",
        "opcoes": [
            "Opção A58",
            "Opção B58",
            "Opção C58",
            "Opção D58"
        ],
        "resposta": "Opção B58",
        "dica": "Dica para a pergunta número 58."
    },
    {
        "pergunta": "Pergunta de exemplo número 59?",
        "opcoes": [
            "Opção A59",
            "Opção B59",
            "Opção C59",
            "Opção D59"
        ],
        "resposta": "Opção B59",
        "dica": "Dica para a pergunta número 59."
    },
    {
        "pergunta": "Pergunta de exemplo número 60?",
        "opcoes": [
            "Opção A60",
            "Opção B60",
            "Opção C60",
            "Opção D60"
        ],
        "resposta": "Opção B60",
        "dica": "Dica para a pergunta número 60."
    },
    {
        "pergunta": "Pergunta de exemplo número 61?",
        "opcoes": [
            "Opção A61",
            "Opção B61",
            "Opção C61",
            "Opção D61"
        ],
        "resposta": "Opção B61",
        "dica": "Dica para a pergunta número 61."
    },
    {
        "pergunta": "Pergunta de exemplo número 62?",
        "opcoes": [
            "Opção A62",
            "Opção B62",
            "Opção C62",
            "Opção D62"
        ],
        "resposta": "Opção B62",
        "dica": "Dica para a pergunta número 62."
    },
    {
        "pergunta": "Pergunta de exemplo número 63?",
        "opcoes": [
            "Opção A63",
            "Opção B63",
            "Opção C63",
            "Opção D63"
        ],
        "resposta": "Opção B63",
        "dica": "Dica para a pergunta número 63."
    },
    {
        "pergunta": "Pergunta de exemplo número 64?",
        "opcoes": [
            "Opção A64",
            "Opção B64",
            "Opção C64",
            "Opção D64"
        ],
        "resposta": "Opção B64",
        "dica": "Dica para a pergunta número 64."
    },
    {
        "pergunta": "Pergunta de exemplo número 65?",
        "opcoes": [
            "Opção A65",
            "Opção B65",
            "Opção C65",
            "Opção D65"
        ],
        "resposta": "Opção B65",
        "dica": "Dica para a pergunta número 65."
    },
    {
        "pergunta": "Pergunta de exemplo número 66?",
        "opcoes": [
            "Opção A66",
            "Opção B66",
            "Opção C66",
            "Opção D66"
        ],
        "resposta": "Opção B66",
        "dica": "Dica para a pergunta número 66."
    },
    {
        "pergunta": "Pergunta de exemplo número 67?",
        "opcoes": [
            "Opção A67",
            "Opção B67",
            "Opção C67",
            "Opção D67"
        ],
        "resposta": "Opção B67",
        "dica": "Dica para a pergunta número 67."
    },
    {
        "pergunta": "Pergunta de exemplo número 68?",
        "opcoes": [
            "Opção A68",
            "Opção B68",
            "Opção C68",
            "Opção D68"
        ],
        "resposta": "Opção B68",
        "dica": "Dica para a pergunta número 68."
    },
    {
        "pergunta": "Pergunta de exemplo número 69?",
        "opcoes": [
            "Opção A69",
            "Opção B69",
            "Opção C69",
            "Opção D69"
        ],
        "resposta": "Opção B69",
        "dica": "Dica para a pergunta número 69."
    },
    {
        "pergunta": "Pergunta de exemplo número 70?",
        "opcoes": [
            "Opção A70",
            "Opção B70",
            "Opção C70",
            "Opção D70"
        ],
        "resposta": "Opção B70",
        "dica": "Dica para a pergunta número 70."
    },
    {
        "pergunta": "Pergunta de exemplo número 71?",
        "opcoes": [
            "Opção A71",
            "Opção B71",
            "Opção C71",
            "Opção D71"
        ],
        "resposta": "Opção B71",
        "dica": "Dica para a pergunta número 71."
    },
    {
        "pergunta": "Pergunta de exemplo número 72?",
        "opcoes": [
            "Opção A72",
            "Opção B72",
            "Opção C72",
            "Opção D72"
        ],
        "resposta": "Opção B72",
        "dica": "Dica para a pergunta número 72."
    },
    {
        "pergunta": "Pergunta de exemplo número 73?",
        "opcoes": [
            "Opção A73",
            "Opção B73",
            "Opção C73",
            "Opção D73"
        ],
        "resposta": "Opção B73",
        "dica": "Dica para a pergunta número 73."
    },
    {
        "pergunta": "Pergunta de exemplo número 74?",
        "opcoes": [
            "Opção A74",
            "Opção B74",
            "Opção C74",
            "Opção D74"
        ],
        "resposta": "Opção B74",
        "dica": "Dica para a pergunta número 74."
    },
    {
        "pergunta": "Pergunta de exemplo número 75?",
        "opcoes": [
            "Opção A75",
            "Opção B75",
            "Opção C75",
            "Opção D75"
        ],
        "resposta": "Opção B75",
        "dica": "Dica para a pergunta número 75."
    },
    {
        "pergunta": "Pergunta de exemplo número 76?",
        "opcoes": [
            "Opção A76",
            "Opção B76",
            "Opção C76",
            "Opção D76"
        ],
        "resposta": "Opção B76",
        "dica": "Dica para a pergunta número 76."
    },
    {
        "pergunta": "Pergunta de exemplo número 77?",
        "opcoes": [
            "Opção A77",
            "Opção B77",
            "Opção C77",
            "Opção D77"
        ],
        "resposta": "Opção B77",
        "dica": "Dica para a pergunta número 77."
    },
    {
        "pergunta": "Pergunta de exemplo número 78?",
        "opcoes": [
            "Opção A78",
            "Opção B78",
            "Opção C78",
            "Opção D78"
        ],
        "resposta": "Opção B78",
        "dica": "Dica para a pergunta número 78."
    },
    {
        "pergunta": "Pergunta de exemplo número 79?",
        "opcoes": [
            "Opção A79",
            "Opção B79",
            "Opção C79",
            "Opção D79"
        ],
        "resposta": "Opção B79",
        "dica": "Dica para a pergunta número 79."
    },
    {
        "pergunta": "Pergunta de exemplo número 80?",
        "opcoes": [
            "Opção A80",
            "Opção B80",
            "Opção C80",
            "Opção D80"
        ],
        "resposta": "Opção B80",
        "dica": "Dica para a pergunta número 80."
    },
    {
        "pergunta": "Pergunta de exemplo número 81?",
        "opcoes": [
            "Opção A81",
            "Opção B81",
            "Opção C81",
            "Opção D81"
        ],
        "resposta": "Opção B81",
        "dica": "Dica para a pergunta número 81."
    },
    {
        "pergunta": "Pergunta de exemplo número 82?",
        "opcoes": [
            "Opção A82",
            "Opção B82",
            "Opção C82",
            "Opção D82"
        ],
        "resposta": "Opção B82",
        "dica": "Dica para a pergunta número 82."
    },
    {
        "pergunta": "Pergunta de exemplo número 83?",
        "opcoes": [
            "Opção A83",
            "Opção B83",
            "Opção C83",
            "Opção D83"
        ],
        "resposta": "Opção B83",
        "dica": "Dica para a pergunta número 83."
    },
    {
        "pergunta": "Pergunta de exemplo número 84?",
        "opcoes": [
            "Opção A84",
            "Opção B84",
            "Opção C84",
            "Opção D84"
        ],
        "resposta": "Opção B84",
        "dica": "Dica para a pergunta número 84."
    },
    {
        "pergunta": "Pergunta de exemplo número 85?",
        "opcoes": [
            "Opção A85",
            "Opção B85",
            "Opção C85",
            "Opção D85"
        ],
        "resposta": "Opção B85",
        "dica": "Dica para a pergunta número 85."
    },
    {
        "pergunta": "Pergunta de exemplo número 86?",
        "opcoes": [
            "Opção A86",
            "Opção B86",
            "Opção C86",
            "Opção D86"
        ],
        "resposta": "Opção B86",
        "dica": "Dica para a pergunta número 86."
    },
    {
        "pergunta": "Pergunta de exemplo número 87?",
        "opcoes": [
            "Opção A87",
            "Opção B87",
            "Opção C87",
            "Opção D87"
        ],
        "resposta": "Opção B87",
        "dica": "Dica para a pergunta número 87."
    },
    {
        "pergunta": "Pergunta de exemplo número 88?",
        "opcoes": [
            "Opção A88",
            "Opção B88",
            "Opção C88",
            "Opção D88"
        ],
        "resposta": "Opção B88",
        "dica": "Dica para a pergunta número 88."
    },
    {
        "pergunta": "Pergunta de exemplo número 89?",
        "opcoes": [
            "Opção A89",
            "Opção B89",
            "Opção C89",
            "Opção D89"
        ],
        "resposta": "Opção B89",
        "dica": "Dica para a pergunta número 89."
    },
    {
        "pergunta": "Pergunta de exemplo número 90?",
        "opcoes": [
            "Opção A90",
            "Opção B90",
            "Opção C90",
            "Opção D90"
        ],
        "resposta": "Opção B90",
        "dica": "Dica para a pergunta número 90."
    },
    {
        "pergunta": "Pergunta de exemplo número 91?",
        "opcoes": [
            "Opção A91",
            "Opção B91",
            "Opção C91",
            "Opção D91"
        ],
        "resposta": "Opção B91",
        "dica": "Dica para a pergunta número 91."
    },
    {
        "pergunta": "Pergunta de exemplo número 92?",
        "opcoes": [
            "Opção A92",
            "Opção B92",
            "Opção C92",
            "Opção D92"
        ],
        "resposta": "Opção B92",
        "dica": "Dica para a pergunta número 92."
    },
    {
        "pergunta": "Pergunta de exemplo número 93?",
        "opcoes": [
            "Opção A93",
            "Opção B93",
            "Opção C93",
            "Opção D93"
        ],
        "resposta": "Opção B93",
        "dica": "Dica para a pergunta número 93."
    },
    {
        "pergunta": "Pergunta de exemplo número 94?",
        "opcoes": [
            "Opção A94",
            "Opção B94",
            "Opção C94",
            "Opção D94"
        ],
        "resposta": "Opção B94",
        "dica": "Dica para a pergunta número 94."
    },
    {
        "pergunta": "Pergunta de exemplo número 95?",
        "opcoes": [
            "Opção A95",
            "Opção B95",
            "Opção C95",
            "Opção D95"
        ],
        "resposta": "Opção B95",
        "dica": "Dica para a pergunta número 95."
    }
]

# Função para sortear uma pergunta ainda não utilizada
def sortear_pergunta(ja_usadas):
    opcoes_disponiveis = [i for i in range(len(perguntas)) if i not in ja_usadas]
    if not opcoes_disponiveis:
        return None
    escolhida = random.choice(opcoes_disponiveis)
    return escolhida, perguntas[escolhida]

# Teste local
if __name__ == "__main__":
    usadas = []
    for _ in range(3):  # Teste de 3 perguntas
        resultado = sortear_pergunta(usadas)
        if resultado:
            indice, pergunta = resultado
            usadas.append(indice)
            print("\nPergunta:", pergunta["pergunta"])
            for i, opcao in enumerate(pergunta["opcoes"]):
                print(f"{i+1}) {opcao}")
        else:
            print("Não há mais perguntas disponíveis.")
