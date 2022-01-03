# PyTCPScan <img src="https://github.com/werdelesmarcio/PyTCPScan/blob/main/Images/icon.png" width=25> 

[![Maintainability](https://api.codeclimate.com/v1/badges/3629bc037bdc9dbf4b71/maintainability)](https://codeclimate.com/github/werdelesmarcio/PyTCPScan/maintainability) <img alt="AppVeyor" src="https://img.shields.io/appveyor/ci/werdelesmarcio/PyTCPScan"> [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_PyTCPScan&metric=alert_status)](https://sonarcloud.io/dashboard?id=werdelesmarcio_PyTCPScan) <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/werdelesmarcio/PyTCPScan"> <img alt="GitHub" src="https://img.shields.io/github/license/werdelesmarcio/PyTCPScan"> <img alt="Twitter URL" src="https://img.shields.io/twitter/url/https/twitter.com/ScorpionInc?style=social">

_Repositório para a aplicação PyTCPScan._

## PyTCPScan
Consiste em uma aplicação voltada para sistemas **GNU/Linux** e tem como finalidade, a 
execução de scaner de portas simples, onde irá verificar quais são as portas estão abertas 
dentro de um range de portas informados por argumentos e retornar **STATUS OPEN**, para os 
casos de as portas varridas estarem abertas. 

Os argumentos informados consistem no endereço de host do alvo que será analisado, seguidos 
das portas inicial e final que comporão o range.

**OBS.: Se sua meta é de escanear apenas uma porta, pode colocar o mesmo valor para 
os dois ultimos parâmetros.**

Está em sua versão 1.2 _(beta)_ e ainda está em fase de desenvolvimento.

## Começando
Estas são as instruções para que você tenha uma cópia do **PyTCPScan** em sua maquina para fins 
de desenvolvimento e teste.

## Pré-requisitos:
* É necessário está rodando uma distro linux;
* Ter instalado em sua máquina o interpretador python na versão 3.xx e o pip3. _(geralmente vem por padrão nas distro linux)_.;
* Fazer o update e upgrade do sistema antes de rodar.

## Instalando:
_Não é necessário instalar o PyTCPScan_

---

_OBS.: Para usar como executável, lembrar de dar permissão de execução_
**sudo chmod +x pytcpscan.py**

---

## Execução 
Para executar a aplicação deve passar o argumento com o host do alvo, a porta inicial
e a porta final. Ele irá verificar quais portas estão com o Status Open.

**./pytcpscan  [target] [init_port] [final_port]**

_Exemplo de Resposta:_

```
             ""8"" 8""""8 8""""8 8""""8                   
  eeeee e    e 8   8    " 8    8 8      eeee eeeee eeeee 
  8   8 8    8 8e  8e     8eeee8 8eeeee 8  8 8   8 8   8 
  8eee8 8eeee8 88  88     88         88 8e   8eee8 8e  8 
  88      88   88  88   e 88     e   88 88   88  8 88  8 
  88      88   88  88eee8 88     8eee88 88e8 88  8 88  8 
----------------------------------------------------------
                                        PyTCPScan ver 1.1
                                      By: Werdeles Soares 
                                     VAULT CYBER SECURITY 
----------------------------------------------------------
 [*]Connecting to Target: xxxxxxxxxxxx.com.br
 [*]Scanning ports between 21 and 110 ...
 
 [!]Please wait, scanning remote host XXX.XX.XXX.XXX
 [*]This may take a while, be patient.
 
 [+]POSITIVE TO Port 21:	Status: OPEN
 [+]POSITIVE TO Port 22:	Status: OPEN
 [+]POSITIVE TO Port 80:	Status: OPEN
--------------------------------------------------
 [!]Scanning Completed in:  0:00:44.584693
--------------------------------------------------

 ---Finished---

```
## Contribuindo:
Leia [as Diretivas de Contribuição](https://github.com/werdelesmarcio/PyTCPScan/blob/master/Archives/CONTRIBUTING.md) para obter mais detalhes de como contribuir para o projeto.

## Autor:
* **Werdeles Marcio de C. Soares** - _Desenvolvedor_

## Licença: 
***Este projeto está sob Licença GPL-3.0.***
Consulte o arquivo [de Licença](https://github.com/werdelesmarcio/PyTCPScan/blob/master/Archives/LICENSE) para obter mais detalhes.

## Agradecimentos:
* Obrigado à todos os que apoiam o projeto de alguma forma.

## Contatos
Se quiser entrar em contato, crie um **issue** no GitHub ou envie um e-mail para werdelesmarcio@gmail.com. Obrigado!

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/PyTCPScan?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/PyTCPScan?style=for-the-badge">

<img src = "https://github.com/werdelesmarcio/PyTCPScan/blob/main/Images/SoftwareLivre.png?raw=true" width =120 align="Right">
<img src = "https://github.com/werdelesmarcio/PyTCPScan/blob/main/Images/PoweredByLinux.png?raw=true" width =80 align="Right">
