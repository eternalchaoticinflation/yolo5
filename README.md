# yolo5
hi the results are here [https://github.com/eternalchaoticinflation/yolo5]

1) table constructed is in [performance_tableQ4.png]
2)qualitative results in step5 is called [Q5qualitative_results_grid.png]
3) model weights are in folder called step1weights, step2weights, step3weights5, step3weights15.
4) you might be able to run some of code, but it would take downloading loads of files and prereqs



refer to the note book we compared four settings:

1. pretrained model with no fine-tuning, 
2. pretrained model fine-tuned for 5 epochs
3. scratch5 model trained for 5 epochs
4. scratch15 model trained for 15 epochs

## Dataset
The road sign dataset annotations were originally in XML format.  
They were converted to YOLO annotation format:

[class_id center_x center_y width height]

The dataset was then split into:
- train
- val
- test

Classes:
- trafficlight
- stop
- speedlimit
- crosswalk

## Performance Comparison

| Model | Training | P | R | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|---:|
| Pretrained, no training | 0 ep | 0.0004 | 0.0266 | 0.000226 | 0.000083 |
| Pretrained | 5 ep | 0.938 | 0.889 | 0.928 | 0.773 |
| Scratch | 5 ep | 0.695 | 0.327 | 0.363 | 0.217 |
| Scratch | 15 ep | 0.746 | 0.599 | 0.663 | 0.500 |

## Discussion

The pretrained model without fine-tuning performed extremely poorly on the road-sign dataset. This is expected because the original pretrained weights were learned on a different dataset, so the class meanings did not match the road-sign classes.

After fine-tuning the pretrained model for 5 epochs, performance improved dramatically. This setting achieved the best overall results:
- Precision = 0.938
- Recall = 0.889
- mAP50 = 0.928
- mAP50-95 = 0.773

Training from scratch for 5 epochs performed much worse than the pretrained model. This shows that random initialization needs more training time and does not adapt as quickly.

Training from scratch for 15 epochs improved the results significantly compared to scratch training for 5 epochs, but it still did not outperform the pretrained model fine-tuned for only 5 epochs.

Overall conclusion:
- pretrained + fine-tuning worked best
- scratch training improved with more epochs
- transfer learning was much more effective than training from scratch for this task

## Qualitative Results

A small subset of test images was evaluated under all four settings.  
The qualitative results matched the quantitative metrics:

- pretrained without fine-tuning produced poor detections
- pretrained after 5 epochs produced the strongest detections
- scratch5 after 5 epochs missed many objects
- scratch15 after 15 epochs improved, but was still weaker than pretrained after 5 epochs
