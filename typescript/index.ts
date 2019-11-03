import {DefaultStatement, Statement} from "./data";

export default class BSGenerator {

    private readonly theme: string;
    private data: Statement;

    constructor(theme: string) {
        this.theme = theme;
        this.data = new DefaultStatement();
    }

    private randomSelect(list: string[]) {
        let randIdx = Math.floor(Math.random() * list.length);
        return list[randIdx];
    }

    private randomNumber(min: number = 0, max: number = 100) {
        return Math.random() * (max - min) + min;
    }

    private randomFamous() {
        const repPrepend = '曾经说过';
        const repAppend = '这不禁令我深思';

        let famous = this.randomSelect(this.data.famous);
        famous = famous.replace(repPrepend, this.randomSelect(this.data.prepend));
        famous = famous.replace(repAppend, this.randomSelect(this.data.append));
        return famous
    }

    private randomState() {
        const repTheme = '主题';

        let statement = this.randomSelect(this.data.state);
        statement = statement.replace(RegExp(repTheme, 'g'), this.theme);
        return statement;
    }

    private addParagraph(paragraph: string) {
        if (paragraph[paragraph.length - 1] === " ") {
            paragraph = paragraph.slice(0, -2)
        }
        return "　　" + paragraph + "。 "
    }

    generate() {
        let article = [];

        let paragraph = "";
        let paragraphLength = 0;
        while (paragraphLength < 6000) {
            let randNum = this.randomNumber();
            if (randNum < 5 && paragraph.length > 200) {
                paragraph = this.addParagraph(paragraph);
                article.push(paragraph);
                paragraph = "";
            } else if (randNum < 20) {
                let state = this.randomFamous();
                paragraphLength = paragraphLength + state.length;
                paragraph = paragraph + state;
            } else {
                let state = this.randomState();
                paragraphLength = paragraphLength + state.length;
                paragraph = paragraph + state;
            }
        }
        paragraph = this.addParagraph(paragraph);
        article.push(paragraph);
        return article.join("\n");
    }
}

