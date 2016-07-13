USE `venic708_financapessoal`;
DROP TABLE fechmovto;
USE `venic708_financapessoal`;
CREATE TABLE `fechmovto` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`datamovto` DATE NOT NULL COMMENT 'Data do Movimento',
	`conta` INT(11) NOT NULL COMMENT 'Conta de Movimento',
	`descricao` VARCHAR(250) NOT NULL DEFAULT '0' COMMENT 'Descrição do Movimento',
	`categoria` INT(11) NOT NULL DEFAULT '0',
	`cenario` INT(11) NOT NULL DEFAULT '0' COMMENT 'Realizado / Futuro',
	`valor` DOUBLE NOT NULL DEFAULT '0' COMMENT 'Valor',
	PRIMARY KEY (`id`),
	INDEX `fk-conta-fech` (`conta`),
	INDEX `fk-cenario-fech` (`cenario`),
	INDEX `fk-subcategoria-fech` (`categoria`),
	CONSTRAINT `fk-cenario-fech` FOREIGN KEY (`cenario`) REFERENCES `cenario` (`id`),
	CONSTRAINT `fk-conta-fech` FOREIGN KEY (`conta`) REFERENCES `conta` (`id`),
	CONSTRAINT `fk-subcategoria-fech` FOREIGN KEY (`categoria`) REFERENCES `categoria` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=0
;

insert into fechmovto(datamovto,conta,descricao,categoria,cenario,valor) 
select datamovto,conta,descricao,categoria,cenario,valor from movtofinanc;