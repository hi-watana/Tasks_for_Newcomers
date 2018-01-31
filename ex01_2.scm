#!/usr/local/bin/gosh
(define (read-file file-name)
  (call-with-input-file file-name port->string-list))

(define (main args)
  (let* ((file-name "NT_113952.1.fasta")
         (lst (read-file file-name))
         (sequence (string->list (apply string-append (cdr lst))))
         (unit-matrix
           (list
             (cons #\A (list 1 0 0 0))
             (cons #\T (list 0 1 0 0))
             (cons #\G (list 0 0 1 0))
             (cons #\C (list 0 0 0 1))
             )
           )
         (vector-list (map (lambda (c)
                             (cdr (assq c unit-matrix)))
                           sequence))
         (count-list (apply map (cons + vector-list)))
         )
    (for-each print (map string-append
                         (list "A: " "T: " "G: " "C: ")
                         (map number->string count-list)))
    )
  0
  )

