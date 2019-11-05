<?php
// bullshit.php by TransparentLC
// “狗屁不通文章生成器”PHP版，加入生成图片功能

// 不准缓存
header('Cache-Control: no-cache, must-revalidate');
header('Pragma: no-cache');
header("Expires: 0");

// 输出自动换行的文本，用于使用gd在图片上添加文字
function imagewraptext($size, $angle, $width, $fontfile, $text) {
    $content = '';
    $letter = preg_split("//u", $text, -1, PREG_SPLIT_NO_EMPTY);
    foreach ($letter as $l) {
        if (($content !== "") && (imagettfbbox($size, $angle, $fontfile, $content . $l)[2] > $width)) $content .= "\n";
        $content .= $l;
    }
    return $content;
}

function 替换标点($文本) {
    $文本 = str_replace(['， ', ', ', ','], '，', $文本);
    $文本 = str_replace(['。 ', '. ', '.'], '。', $文本);
    $文本 = str_replace(['： ', ': ', ':'], '：', $文本);
    $文本 = str_replace(['？ ', '? ', '?'], '？', $文本);
    return $文本;
}

function 垫话($文本) {
    global $前面垫话, $后面垫话;
    $文本 = str_replace('a', $前面垫话[array_rand($前面垫话)], $文本);
    $文本 = str_replace('b', $后面垫话[array_rand($后面垫话)], $文本);
    return $文本;
}

// 读取数据
$数据 = json_decode(file_get_contents('./data.json'), true);
$名人名言 = $数据['famous']; // a和b分别是前面和后面垫话
$前面垫话 = $数据['before'];
$后面垫话 = $数据['after'];
$废话 = $数据['bosh'];

// 设定参数
$主题 = empty($_GET['word']) ? '学生会退会' : $_GET['word'];
$长度 = (empty($_GET['length']) || !is_numeric($_GET['length'])) ? 1000 : intval($_GET['length']);
$图片宽度 = (empty($_GET['width']) || !is_numeric($_GET['width'])) ? 0 : intval($_GET['width']);
$字号 = (empty($_GET['fontsize']) || !is_numeric($_GET['fontsize'])) ? 16 : intval($_GET['fontsize']);
$字体路径 = './方正硬笔行书简体.ttf';
$边距 = 20;
$行间距 = .9;

// 设定上限
if ($长度 > 65536) $长度 = 65536;
if ($图片宽度 && $长度 > 2048) $长度 = 2048;
if ($图片宽度 > 1024) $图片宽度 = 1024;

// 生成文章
$文章 = [];
$段落 = '';
$段落总长度 = 0;
while ($段落总长度 < $长度) {
    $分支 = mt_rand(0, 100);
    if ($分支 < 5 && mb_strlen($段落) > 50) { // 另起一段，每段至少五十字
        $文章[] = '　　' . mb_substr($段落, 0, mb_strlen($段落) - 1) . '。';
        $文本 = '';
        $段落 = '';
    } elseif ($分支 < 20) { // 名人名言
        $文本 = 替换标点(垫话($名人名言[array_rand($名人名言)]));
    } else { // 废话
        $文本 = 替换标点($废话[array_rand($废话)]);
    }
    $段落 .= $文本;
    $段落总长度 += mb_strlen($文本);
}

// 把最后一段也加上
$文章[] = '　　' . mb_substr($段落, 0, mb_strlen($段落) - 1) . '。';
$文章 = str_replace('x', $主题, join("\n", $文章));

// 不生成图片的话，直接输出文本
if (!$图片宽度) {
    header('Content-Type: text/plain; charset=UTF-8');
    die($文章);
}

// 输出图片
$文章 = imagewraptext($字号, 0, $图片宽度 - $边距 * 2, $字体路径, $文章);
$文本框 = imageftbbox($字号, 0, $字体路径, $文章, ['linespacing' => $行间距]);
$图片 = imagecreatetruecolor($图片宽度, $文本框[1] - $文本框[5] + $边距 * 2);
imagefill($图片, 0, 0, imagecolorallocate($图片, 255, 255, 255));
imagefttext($图片, $字号, 0, $边距, $边距 + $字号, imagecolorallocate($图片, 0, 0, 0), $字体路径, $文章, ['linespacing' => $行间距]);
header('Content-Type: image/png');
imagepng($图片, null, 1);
imagedestroy($图片);
?>