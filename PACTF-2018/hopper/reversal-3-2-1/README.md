  

000000000040062d <bananagrams3>:
  40062d:	55                   	push   %rbp
  40062e:	48 89 e5             	mov    %rsp,%rbp
  400631:	48 83 ec 10          	sub    $0x10,%rsp
  400635:	c7 45 fc 05 00 00 00 	movl   $0x5,-0x4(%rbp)
  40063c:	eb 13                	jmp    400651 <bananagrams3+0x24>
  40063e:	b8 04 00 00 00       	mov    $0x4,%eax
  400643:	99                   	cltd   
  400644:	f7 7d fc             	idivl  -0x4(%rbp)
  400647:	89 d0                	mov    %edx,%eax
  400649:	85 c0                	test   %eax,%eax
  40064b:	74 26                	je     400673 <bananagrams3+0x46>
  40064d:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
  400651:	8b 45 fc             	mov    -0x4(%rbp),%eax
  400654:	0f af 45 fc          	imul   -0x4(%rbp),%eax
  400658:	83 f8 03             	cmp    $0x3,%eax
  40065b:	7e e1                	jle    40063e <bananagrams3+0x11>
  40065d:	be 04 00 00 00       	mov    $0x4,%esi
  400662:	bf f4 0c 40 00       	mov    $0x400cf4,%edi
  400667:	b8 00 00 00 00       	mov    $0x0,%eax
  40066c:	e8 3f fe ff ff       	callq  4004b0 <printf@plt>
  400671:	eb 01                	jmp    400674 <bananagrams3+0x47>
  400673:	90                   	nop
  400674:	c9                   	leaveq 
  400675:	c3                   	retq

000000000040067d <bananagrams5>:
  40067d:	55                   	push   %rbp
  40067e:	48 89 e5             	mov    %rsp,%rbp
  400681:	bf f8 0c 40 00       	mov    $0x400cf8,%edi
  400686:	b8 00 00 00 00       	mov    $0x0,%eax
  40068b:	e8 20 fe ff ff       	callq  4004b0 <printf@plt>
  400690:	90                   	nop
  400691:	5d                   	pop    %rbp
  400692:	c3                   	retq   

0000000000400693 <bananagrams6>:
  400693:	55                   	push   %rbp
  400694:	48 89 e5             	mov    %rsp,%rbp
  400697:	48 83 ec 10          	sub    $0x10,%rsp
  40069b:	c7 45 fc 02 00 00 00 	movl   $0x2,-0x4(%rbp)
  4006a2:	eb 13                	jmp    4006b7 <bananagrams6+0x24>
  4006a4:	b8 02 00 00 00       	mov    $0x2,%eax
  4006a9:	99                   	cltd   
  4006aa:	f7 7d fc             	idivl  -0x4(%rbp)
  4006ad:	89 d0                	mov    %edx,%eax
  4006af:	85 c0                	test   %eax,%eax
  4006b1:	74 25                	je     4006d8 <bananagrams6+0x45>
  4006b3:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
  4006b7:	8b 45 fc             	mov    -0x4(%rbp),%eax
  4006ba:	0f af 45 fc          	imul   -0x4(%rbp),%eax
  4006be:	85 c0                	test   %eax,%eax
  4006c0:	7e e2                	jle    4006a4 <bananagrams6+0x11>
  4006c2:	be 02 00 00 00       	mov    $0x2,%esi
  4006c7:	bf f4 0c 40 00       	mov    $0x400cf4,%edi
  4006cc:	b8 00 00 00 00       	mov    $0x0,%eax
  4006d1:	e8 da fd ff ff       	callq  4004b0 <printf@plt>
  4006d6:	eb 01                	jmp    4006d9 <bananagrams6+0x46>
  4006d8:	90                   	nop
  4006d9:	c9                   	leaveq 
  4006da:	c3                   	retq

000000000040070c <bananagrams14>:
  40070c:	55                   	push   %rbp
  40070d:	48 89 e5             	mov    %rsp,%rbp
  400710:	bf fb 0c 40 00       	mov    $0x400cfb,%edi
  400715:	b8 00 00 00 00       	mov    $0x0,%eax
  40071a:	e8 91 fd ff ff       	callq  4004b0 <printf@plt>
  40071f:	90                   	nop
  400720:	5d                   	pop    %rbp
  400721:	c3                   	retq

000000000040075a <bananagrams23>:
  40075a:	55                   	push   %rbp
  40075b:	48 89 e5             	mov    %rsp,%rbp
  40075e:	bf 04 0d 40 00       	mov    $0x400d04,%edi
  400763:	b8 00 00 00 00       	mov    $0x0,%eax
  400768:	e8 43 fd ff ff       	callq  4004b0 <printf@plt>
  40076d:	90                   	nop
  40076e:	5d                   	pop    %rbp
  40076f:	c3                   	retq 

00000000004007a1 <bananagrams31>:
  4007a1:	55                   	push   %rbp
  4007a2:	48 89 e5             	mov    %rsp,%rbp
  4007a5:	48 83 ec 10          	sub    $0x10,%rsp
  4007a9:	c7 45 fc 02 00 00 00 	movl   $0x2,-0x4(%rbp)
  4007b0:	eb 13                	jmp    4007c5 <bananagrams31+0x24>
  4007b2:	b8 02 00 00 00       	mov    $0x2,%eax
  4007b7:	99                   	cltd   
  4007b8:	f7 7d fc             	idivl  -0x4(%rbp)
  4007bb:	89 d0                	mov    %edx,%eax
  4007bd:	85 c0                	test   %eax,%eax
  4007bf:	74 26                	je     4007e7 <bananagrams31+0x46>
  4007c1:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
  4007c5:	8b 45 fc             	mov    -0x4(%rbp),%eax
  4007c8:	0f af 45 fc          	imul   -0x4(%rbp),%eax
  4007cc:	83 f8 02             	cmp    $0x2,%eax
  4007cf:	7e e1                	jle    4007b2 <bananagrams31+0x11>
  4007d1:	be 02 00 00 00       	mov    $0x2,%esi
  4007d6:	bf f4 0c 40 00       	mov    $0x400cf4,%edi
  4007db:	b8 00 00 00 00       	mov    $0x0,%eax
  4007e0:	e8 cb fc ff ff       	callq  4004b0 <printf@plt>
  4007e5:	eb 01                	jmp    4007e8 <bananagrams31+0x47>
  4007e7:	90                   	nop
  4007e8:	c9                   	leaveq 
  4007e9:	c3                   	retq

0000000000400806 <bananagrams36>:
  400806:	55                   	push   %rbp
  400807:	48 89 e5             	mov    %rsp,%rbp
  40080a:	bf 09 0d 40 00       	mov    $0x400d09,%edi
  40080f:	b8 00 00 00 00       	mov    $0x0,%eax
  400814:	e8 97 fc ff ff       	callq  4004b0 <printf@plt>
  400819:	90                   	nop
  40081a:	5d                   	pop    %rbp
  40081b:	c3                   	retq  

000000000040082a <bananagrams39>:
  40082a:	55                   	push   %rbp
  40082b:	48 89 e5             	mov    %rsp,%rbp
  40082e:	48 83 ec 10          	sub    $0x10,%rsp
  400832:	c7 45 fc 02 00 00 00 	movl   $0x2,-0x4(%rbp)
  400839:	eb 13                	jmp    40084e <bananagrams39+0x24>
  40083b:	b8 02 00 00 00       	mov    $0x2,%eax
  400840:	99                   	cltd   
  400841:	f7 7d fc             	idivl  -0x4(%rbp)
  400844:	89 d0                	mov    %edx,%eax
  400846:	85 c0                	test   %eax,%eax
  400848:	74 26                	je     400870 <bananagrams39+0x46>
  40084a:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
  40084e:	8b 45 fc             	mov    -0x4(%rbp),%eax
  400851:	0f af 45 fc          	imul   -0x4(%rbp),%eax
  400855:	83 f8 64             	cmp    $0x64,%eax
  400858:	7e e1                	jle    40083b <bananagrams39+0x11>
  40085a:	be 02 00 00 00       	mov    $0x2,%esi
  40085f:	bf f4 0c 40 00       	mov    $0x400cf4,%edi
  400864:	b8 00 00 00 00       	mov    $0x0,%eax
  400869:	e8 42 fc ff ff       	callq  4004b0 <printf@plt>
  40086e:	eb 01                	jmp    400871 <bananagrams39+0x47>
  400870:	90                   	nop
  400871:	c9                   	leaveq 
  400872:	c3                   	retq 

0000000000400881 <bananagrams42>:
  400881:	55                   	push   %rbp
  400882:	48 89 e5             	mov    %rsp,%rbp
  400885:	bf 0d 0d 40 00       	mov    $0x400d0d,%edi
  40088a:	b8 00 00 00 00       	mov    $0x0,%eax
  40088f:	e8 1c fc ff ff       	callq  4004b0 <printf@plt>
  400894:	90                   	nop
  400895:	5d                   	pop    %rbp
  400896:	c3                   	retq   

0000000000400897 <bananagrams43>:
  400897:	55                   	push   %rbp
  400898:	48 89 e5             	mov    %rsp,%rbp
  40089b:	bf 64 00 00 00       	mov    $0x64,%edi
  4008a0:	e8 eb fb ff ff       	callq  400490 <putchar@plt>
  4008a5:	90                   	nop
  4008a6:	5d                   	pop    %rbp
  4008a7:	c3                   	retq  

00000000004008b6 <bananagrams46>:
  4008b6:	55                   	push   %rbp
  4008b7:	48 89 e5             	mov    %rsp,%rbp
  4008ba:	bf 13 0d 40 00       	mov    $0x400d13,%edi
  4008bf:	b8 00 00 00 00       	mov    $0x0,%eax
  4008c4:	e8 e7 fb ff ff       	callq  4004b0 <printf@plt>
  4008c9:	90                   	nop
  4008ca:	5d                   	pop    %rbp
  4008cb:	c3                   	retq 

00000000004008d3 <bananagrams48>:
  4008d3:	55                   	push   %rbp
  4008d4:	48 89 e5             	mov    %rsp,%rbp
  4008d7:	48 83 ec 10          	sub    $0x10,%rsp
  4008db:	c7 45 fc 02 00 00 00 	movl   $0x2,-0x4(%rbp)
  4008e2:	eb 13                	jmp    4008f7 <bananagrams48+0x24>
  4008e4:	b8 02 00 00 00       	mov    $0x2,%eax
  4008e9:	99                   	cltd   
  4008ea:	f7 7d fc             	idivl  -0x4(%rbp)
  4008ed:	89 d0                	mov    %edx,%eax
  4008ef:	85 c0                	test   %eax,%eax
  4008f1:	74 26                	je     400919 <bananagrams48+0x46>
  4008f3:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
  4008f7:	8b 45 fc             	mov    -0x4(%rbp),%eax
  4008fa:	0f af 45 fc          	imul   -0x4(%rbp),%eax
  4008fe:	83 f8 02             	cmp    $0x2,%eax
  400901:	7e e1                	jle    4008e4 <bananagrams48+0x11>
  400903:	be 01 00 00 00       	mov    $0x1,%esi
  400908:	bf f4 0c 40 00       	mov    $0x400cf4,%edi
  40090d:	b8 00 00 00 00       	mov    $0x0,%eax
  400912:	e8 99 fb ff ff       	callq  4004b0 <printf@plt>
  400917:	eb 01                	jmp    40091a <bananagrams48+0x47>
  400919:	90                   	nop
  40091a:	c9                   	leaveq 
  40091b:	c3                   	retq 

0000000000400931 <bananagrams52>:
  400931:	55                   	push   %rbp
  400932:	48 89 e5             	mov    %rsp,%rbp
  400935:	bf 18 0d 40 00       	mov    $0x400d18,%edi
  40093a:	b8 00 00 00 00       	mov    $0x0,%eax
  40093f:	e8 6c fb ff ff       	callq  4004b0 <printf@plt>
  400944:	90                   	nop
  400945:	5d                   	pop    %rbp
  400946:	c3                   	retq  

000000000040094e <bananagrams54>:
  40094e:	55                   	push   %rbp
  40094f:	48 89 e5             	mov    %rsp,%rbp
  400952:	bf 1d 0d 40 00       	mov    $0x400d1d,%edi
  400957:	b8 00 00 00 00       	mov    $0x0,%eax
  40095c:	e8 4f fb ff ff       	callq  4004b0 <printf@plt>
  400961:	90                   	nop
  400962:	5d                   	pop    %rbp
  400963:	c3                   	retq  

000000000040096b <bananagrams56>:
  40096b:	55                   	push   %rbp
  40096c:	48 89 e5             	mov    %rsp,%rbp
  40096f:	bf 22 0d 40 00       	mov    $0x400d22,%edi
  400974:	b8 00 00 00 00       	mov    $0x0,%eax
  400979:	e8 32 fb ff ff       	callq  4004b0 <printf@plt>
  40097e:	90                   	nop
  40097f:	5d                   	pop    %rbp
  400980:	c3                   	retq     

000000000040099d <bananagrams61>:
  40099d:	55                   	push   %rbp
  40099e:	48 89 e5             	mov    %rsp,%rbp
  4009a1:	bf 26 0d 40 00       	mov    $0x400d26,%edi
  4009a6:	b8 00 00 00 00       	mov    $0x0,%eax
  4009ab:	e8 00 fb ff ff       	callq  4004b0 <printf@plt>
  4009b0:	90                   	nop
  4009b1:	5d                   	pop    %rbp
  4009b2:	c3                   	retq   

00000000004009b3 <bananagrams62>:
  4009b3:	55                   	push   %rbp
  4009b4:	48 89 e5             	mov    %rsp,%rbp
  4009b7:	be 02 00 00 00       	mov    $0x2,%esi
  4009bc:	bf f4 0c 40 00       	mov    $0x400cf4,%edi
  4009c1:	b8 00 00 00 00       	mov    $0x0,%eax
  4009c6:	e8 e5 fa ff ff       	callq  4004b0 <printf@plt>
  4009cb:	90                   	nop
  4009cc:	5d                   	pop    %rbp
  4009cd:	c3                   	retq   

0000000000400a0d <bananagrams72>:
  400a0d:	55                   	push   %rbp
  400a0e:	48 89 e5             	mov    %rsp,%rbp
  400a11:	bf 2b 0d 40 00       	mov    $0x400d2b,%edi
  400a16:	b8 00 00 00 00       	mov    $0x0,%eax
  400a1b:	e8 90 fa ff ff       	callq  4004b0 <printf@plt>
  400a20:	90                   	nop
  400a21:	5d                   	pop    %rbp
  400a22:	c3                   	retq   

0000000000400a62 <bananagrams82>:
  400a62:	55                   	push   %rbp
  400a63:	48 89 e5             	mov    %rsp,%rbp
  400a66:	bf 2f 0d 40 00       	mov    $0x400d2f,%edi
  400a6b:	b8 00 00 00 00       	mov    $0x0,%eax
  400a70:	e8 3b fa ff ff       	callq  4004b0 <printf@plt>
  400a75:	90                   	nop
  400a76:	5d                   	pop    %rbp
  400a77:	c3                   	retq   

0000000000400a9b <bananagrams88>:
  400a9b:	55                   	push   %rbp
  400a9c:	48 89 e5             	mov    %rsp,%rbp
  400a9f:	48 83 ec 10          	sub    $0x10,%rsp
  400aa3:	c7 45 fc 02 00 00 00 	movl   $0x2,-0x4(%rbp)
  400aaa:	eb 13                	jmp    400abf <bananagrams88+0x24>
  400aac:	b8 02 00 00 00       	mov    $0x2,%eax
  400ab1:	99                   	cltd   
  400ab2:	f7 7d fc             	idivl  -0x4(%rbp)
  400ab5:	89 d0                	mov    %edx,%eax
  400ab7:	85 c0                	test   %eax,%eax
  400ab9:	74 26                	je     400ae1 <bananagrams88+0x46>
  400abb:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
  400abf:	8b 45 fc             	mov    -0x4(%rbp),%eax
  400ac2:	0f af 45 fc          	imul   -0x4(%rbp),%eax
  400ac6:	83 f8 64             	cmp    $0x64,%eax
  400ac9:	7e e1                	jle    400aac <bananagrams88+0x11>
  400acb:	be 02 00 00 00       	mov    $0x2,%esi
  400ad0:	bf f4 0c 40 00       	mov    $0x400cf4,%edi
  400ad5:	b8 00 00 00 00       	mov    $0x0,%eax
  400ada:	e8 d1 f9 ff ff       	callq  4004b0 <printf@plt>
  400adf:	eb 01                	jmp    400ae2 <bananagrams88+0x47>
  400ae1:	90                   	nop
  400ae2:	c9                   	leaveq 
  400ae3:	c3                   	retq   

0000000000400aeb <bananagrams90>:
  400aeb:	55                   	push   %rbp
  400aec:	48 89 e5             	mov    %rsp,%rbp
  400aef:	bf 26 0d 40 00       	mov    $0x400d26,%edi
  400af4:	b8 00 00 00 00       	mov    $0x0,%eax
  400af9:	e8 b2 f9 ff ff       	callq  4004b0 <printf@plt>
  400afe:	90                   	nop
  400aff:	5d                   	pop    %rbp
  400b00:	c3                   	retq    

0000000000400b08 <bananagrams92>:
  400b08:	55                   	push   %rbp
  400b09:	48 89 e5             	mov    %rsp,%rbp
  400b0c:	bf 34 0d 40 00       	mov    $0x400d34,%edi
  400b11:	b8 00 00 00 00       	mov    $0x0,%eax
  400b16:	e8 95 f9 ff ff       	callq  4004b0 <printf@plt>
  400b1b:	90                   	nop
  400b1c:	5d                   	pop    %rbp
  400b1d:	c3                   	retq   

0000000000400b1e <bananagrams93>:
  400b1e:	55                   	push   %rbp
  400b1f:	48 89 e5             	mov    %rsp,%rbp
  400b22:	bf 39 0d 40 00       	mov    $0x400d39,%edi
  400b27:	b8 00 00 00 00       	mov    $0x0,%eax
  400b2c:	e8 7f f9 ff ff       	callq  4004b0 <printf@plt>
  400b31:	90                   	nop
  400b32:	5d                   	pop    %rbp
  400b33:	c3                   	retq   

0000000000400b3b <bananagrams95>:
  400b3b:	55                   	push   %rbp
  400b3c:	48 89 e5             	mov    %rsp,%rbp
  400b3f:	bf 4b 0d 40 00       	mov    $0x400d4b,%edi
  400b44:	b8 00 00 00 00       	mov    $0x0,%eax
  400b49:	e8 62 f9 ff ff       	callq  4004b0 <printf@plt>
  400b4e:	90                   	nop
  400b4f:	5d                   	pop    %rbp
  400b50:	c3                   	retq   

0000000000400b51 <bananagrams96>:
  400b51:	55                   	push   %rbp
  400b52:	48 89 e5             	mov    %rsp,%rbp
  400b55:	48 83 ec 10          	sub    $0x10,%rsp
  400b59:	c7 45 fc 04 00 00 00 	movl   $0x4,-0x4(%rbp)
  400b60:	eb 13                	jmp    400b75 <bananagrams96+0x24>
  400b62:	b8 02 00 00 00       	mov    $0x2,%eax
  400b67:	99                   	cltd   
  400b68:	f7 7d fc             	idivl  -0x4(%rbp)
  400b6b:	89 d0                	mov    %edx,%eax
  400b6d:	85 c0                	test   %eax,%eax
  400b6f:	74 26                	je     400b97 <bananagrams96+0x46>
  400b71:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
  400b75:	8b 45 fc             	mov    -0x4(%rbp),%eax
  400b78:	0f af 45 fc          	imul   -0x4(%rbp),%eax
  400b7c:	83 f8 05             	cmp    $0x5,%eax
  400b7f:	7e e1                	jle    400b62 <bananagrams96+0x11>
  400b81:	be 01 00 00 00       	mov    $0x1,%esi
  400b86:	bf f4 0c 40 00       	mov    $0x400cf4,%edi
  400b8b:	b8 00 00 00 00       	mov    $0x0,%eax
  400b90:	e8 1b f9 ff ff       	callq  4004b0 <printf@plt>
  400b95:	eb 01                	jmp    400b98 <bananagrams96+0x47>
  400b97:	90                   	nop
  400b98:	c9                   	leaveq 
  400b99:	c3                   	retq   

b *main+166
b *bananagrams3+71
b *bananagrams5+19
b *bananagrams6+70
b *bananagrams14+19
b *bananagrams23+19
b *bananagrams31+71
b *bananagrams36+19
b *bananagrams39+71
b *bananagrams42+19
b *bananagrams43+14
b *bananagrams46+19
b *bananagrams48+71
b *bananagrams52+19
b *bananagrams54+19
b *bananagrams56+19
b *bananagrams61+19
b *bananagrams62+19
b *bananagrams72+19
b *bananagrams82+19
b *bananagrams88+71
b *bananagrams90+19
b *bananagrams92+19
b *bananagrams93+19
b *bananagrams95+19
b *bananagrams96+71

7 2 18 9 10 4 19 13 11 5 22 16 24
36 5 72 42 43 14 82 52 46 23 92 61 95 10

for i in 7 2 18 9 10 4 19 13 11 5 22 16 24; do tail -c +15 out$i.txt; done
scrambled_a_byte_902_102__910_917_102_104_1042

r > out1.txt
jump bananagrams3
jump *main+166
c
r > out2.txt
jump bananagrams5
jump *main+166
c
r > out3.txt
jump bananagrams6
jump *main+166
c
r > out4.txt
jump bananagrams14
jump *main+166
c
r > out5.txt
jump bananagrams23
jump *main+166
c
r > out6.txt
jump bananagrams31
jump *main+166
c
r > out7.txt
jump bananagrams36
jump *main+166
c
r > out8.txt
jump bananagrams39
jump *main+166
c
r > out9.txt
jump bananagrams42
jump *main+166
c
r > out10.txt
jump bananagrams43
jump *main+166
c
r > out11.txt
jump bananagrams46
jump *main+166
c
r > out12.txt
jump bananagrams48
jump *main+166
c
r > out13.txt
jump bananagrams52
jump *main+166
c
r > out14.txt
jump bananagrams54
jump *main+166
c
r > out15.txt
jump bananagrams56
jump *main+166
c
r > out16.txt
jump bananagrams61
jump *main+166
c
r > out17.txt
jump bananagrams62
jump *main+166
c
r > out18.txt
jump bananagrams72
jump *main+166
c
r > out19.txt
jump bananagrams82
jump *main+166
c
r > out20.txt
jump bananagrams88
jump *main+166
c
r > out21.txt
jump bananagrams90
jump *main+166
c
r > out22.txt
jump bananagrams92
jump *main+166
c
r > out23.txt
jump bananagrams93
jump *main+166
c
r > out24.txt
jump bananagrams95
jump *main+166
c
r > out25.txt
jump bananagrams96
jump *main+166
c